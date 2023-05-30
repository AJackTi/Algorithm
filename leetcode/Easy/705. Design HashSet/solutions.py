class MyHashSet:
    def __init__(self):
        self.SIZE = 1000
        self.my_buckets = [[] for _ in range(self.SIZE)]
        
    def hash(self, key):
        return key % self.SIZE

    def add(self, key: int) -> None:
        hash_key = self.hash(key=key)
        if not self.contains(key):
            self.my_buckets[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = self.hash(key=key)
        if self.contains(key):
            self.my_buckets[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        hash_key = self.hash(key=key)
        return key in self.my_buckets[hash_key]

myHashSet = MyHashSet()
print(myHashSet.add(1))
print(myHashSet.add(2))
print(myHashSet.contains(1))
print(myHashSet.contains(3))
print(myHashSet.add(2))
print(myHashSet.contains(2))
print(myHashSet.remove(2))
print(myHashSet.contains(2))
print(myHashSet.my_buckets)