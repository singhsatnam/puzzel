class LRUCache(dict):
    def __init__(self, capacity):
        super().__init__()
        self.available = capacity

    def get(self, key):
        if key in self:
            val = self.pop(key)
            self[key] = val
            return val
        else:
            return -1

    def set(self, key, value):
        if key in self:
            self.pop(key)
            self.available += 1
        else:
            if self.available == 0:
                self.pop(next(iter(self)))
                self.available += 1
        self[key] = value
        self.available -= 1


obj = LRUCache(2)
obj.set(2, 2)
obj.set(3, 3)
obj.set('x', 4)
assert obj.get(2) == -1
obj.set(2, 2)
assert obj.get(3) == -1
assert obj.get(2) == 2
assert obj.get('x') == 4
