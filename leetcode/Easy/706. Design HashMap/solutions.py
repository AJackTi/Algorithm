class MyHashMap:
    def __init__(self):
        self.data = [-1]*int(1e6+1)

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]
        
    def remove(self, key: int) -> None:
        self.data[key] = -1
