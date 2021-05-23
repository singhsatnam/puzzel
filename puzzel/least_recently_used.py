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
