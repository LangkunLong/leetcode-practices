#include <map>
#include <iostream>
#include <cassert>

template<typename K, typename V>
class interval_map {
    friend void IntervalMapTest();
    V m_valBegin;
    std::map<K, V> m_map;

public:
    // constructor associates whole range of K with val
    template<typename V_forward>
    interval_map(V_forward&& val)
        : m_valBegin(std::forward<V_forward>(val)) {}

    // Assign value val to interval [keyBegin, keyEnd).
    // Overwrite previous values in this interval.
    // Conforming to the C++ Standard Library conventions, the interval
    // includes keyBegin, but excludes keyEnd.
    // If !( keyBegin < keyEnd ), this designates an empty interval,
    // and assign must do nothing.
    template<typename V_forward>
    void assign(K const& keyBegin, K const& keyEnd, V_forward&& val)
        requires (std::is_same<std::remove_cvref_t<V_forward>, V>::value)
    {
        if (!(keyBegin < keyEnd)) {
            return; // Empty interval, do nothing
        }

        // Get iterator to the first element not less than keyBegin
        auto itBegin = m_map.lower_bound(keyBegin);
        // Get iterator to the first element not less than keyEnd
        auto itEnd = m_map.lower_bound(keyEnd);

        // Check the value just before keyBegin (m_valBegin if nothing before it)
        V valBeforeBegin = (itBegin != m_map.begin()) ? std::prev(itBegin)->second : m_valBegin;

        // Check the value at keyEnd (m_valBegin if no exact match)
        V valAtEnd = (itEnd != m_map.end() && itEnd->first == keyEnd) ? itEnd->second
                      : (itEnd != m_map.begin() ? std::prev(itEnd)->second : m_valBegin);

        // Erase the range [keyBegin, keyEnd) because we will overwrite it
        m_map.erase(itBegin, itEnd);

        // Insert keyEnd with the value that was at keyEnd if it's not equal to the new value
        if (!(val == valAtEnd)) {
            m_map[keyEnd] = valAtEnd;
        }

        // Insert keyBegin with the new value if it's not equal to the value before it
        if (!(val == valBeforeBegin)) {
            m_map[keyBegin] = std::forward<V_forward>(val);
        }
    }
};
