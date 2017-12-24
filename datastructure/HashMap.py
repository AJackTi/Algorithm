class HashMap():
    def __init__(self):
        self.size = 10
        self.arr = [ [] for i in range(0,10)]
    
    def _get_index(self, key):
        sum_add = 0
        for char in str(key):
            sum_add += ord(char)
        
        return sum_add % self.size
        
    def insert(self, key, value):
        index = self._get_index(key)
        key_hash = [key, value]
        if self.find(key) != None:
            self.arr[index].remove(self.find(key))
            self.arr[index].append(key_hash)
        else:
            self.arr[index].append(key_hash)

    def find(self, key):
        index = self._get_index(key)
        count = 0
        for arr in self.arr[index]:
            if arr[count] == key:
                return self.arr[index][count]
            count += 1
        return None

    def delete(self, key):
        index = self._get_index(key)
        if self.find(key) != None:
            self.arr[index].remove(self.find(key))
            return True
        else:
            return False            

    def presentation(self):
        print "PRINT HASH"
        for arr in self.arr:
            if arr:
                print arr
    
hash = HashMap()
hash.insert("ABCDEF", 20)
hash.insert("abcdef", 30)
hash.insert("AJack Ti", 20)
hash.insert("AJack Ti", 40)
hash.presentation()

print "FIND: " + str(hash.find("AJack Ti"))
print "DELETE AJack Ti" 
hash.delete("AJack Ti")
print "Again: "
hash.presentation()