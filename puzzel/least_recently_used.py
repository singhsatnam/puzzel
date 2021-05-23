import collections


class LRUCache(dict):
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v  # set key as the newest one
        return v

    def set(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:  # self.dic is full
                self.dic.popitem(last=False)
        self.dic[key] = value


obj = LRUCache(2)
obj.set(2, 2)
obj.set(3, 3)
obj.set('x', 4)
assert obj.get(2) == -1
obj.set(2, 2)
assert obj.get(3) == -1
assert obj.get(2) == 2
assert obj.get('x') == 4

# class Node:
# def __init__(self, k, v):
#     self.key = k
#     self.val = v
#     self.prev = None
#     self.next = None
#
# class LRUCache:
# def __init__(self, capacity):
#     self.capacity = capacity
#     self.dic = dict()
#     self.head = Node(0, 0)
#     self.tail = Node(0, 0)
#     self.head.next = self.tail
#     self.tail.prev = self.head
#
# def get(self, key):
#     if key in self.dic:
#         n = self.dic[key]
#         self._remove(n)
#         self._add(n)
#         return n.val
#     return -1
#
# def set(self, key, value):
#     if key in self.dic:
#         self._remove(self.dic[key])
#     n = Node(key, value)
#     self._add(n)
#     self.dic[key] = n
#     if len(self.dic) > self.capacity:
#         n = self.head.next
#         self._remove(n)
#         del self.dic[n.key]
#
# def _remove(self, node):
#     p = node.prev
#     n = node.next
#     p.next = n
#     n.prev = p
#
# def _add(self, node):
#     p = self.tail.prev
#     p.next = node
#     self.tail.prev = node
#     node.prev = p
#     node.next = self.tail