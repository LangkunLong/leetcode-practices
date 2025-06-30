class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # preserve order of characters
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False
        if s == t:
            return True

        # i need a mapping: p -> t at index 0, 2, a map to i at index 2, e map to l at index 4, r map to e at index 5, if all mappings are successful, then return true 
        # don't need order since i'm traversing 
        s_map_dict = dict()
        t_map_dict = dict()
        for i in range(len(s)):
            s_map_dict[s[i]] = t[i]
            t_map_dict[t[i]] = s[i]
        
        for i in range(len(s)):
            if s_map_dict[s[i]] != t[i] or t_map_dict[t[i]] != s[i]:
                return False
        
        return True
        
        # is there a better solution?
        

