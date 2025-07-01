# doubly linked lists
# cannot use an array because need to shift most recently used in the front ~O(n) time 
# O(1) random access using map, then using linked lists to order keys for eviction 
# insert recently used node at the head, use tail node to get the LRU node

# data structures:
# map <key, node reference> : we are reordering the nodes
# doubley linked list: key, value, prev, next

# tricky part is remember to delete from cache[node.key], since the capcacity is tracked from the dictionary,
# not the linked list, if just delete the node itself. like del node, the dangling pointer is still there

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = dict() 
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            # move node to most recently used besides head, need to remove from current position and insert
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        # insert into head
        return -1

    def put(self, key: int, value: int) -> None:
        # if node exists, update the value and move to mru
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            # if we reached limit, evict from tail
            if len(self.cache) == self.size:
                lru_node = self.tail.prev
                self.remove(lru_node)
                del self.cache[lru_node.key]
            # insert a new node at head
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

    # insert any node next to head 
    def insert(self, node):
        node_next = self.head.next
        node.prev = self.head
        node.next = node_next
        node_next.prev = node
        self.head.next = node

    # remove a node at any position, just deleting the link connection, still might need the node for insert
    def remove(self, node):
        node_prev, node_next = node.prev, node.next
        node_prev.next = node_next
        node_next.prev = node_prev
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)