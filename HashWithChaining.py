import random

# using universal hash function  - hash = ((a * key + b) % p ) % size
# where a , b are random and p is a large prime

 #[("Hash1", "Value1"), ("Hash2", "Value2")]
class HashWithChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.p = 10**9 + 7  # A large prime number
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def getHash(self,key):
        if isinstance(key,str):
            key = self.convert_str_to_int(key)
        return ((self.a * key + self.b) % self.p) % self.size
    
    
    def insert(self, key, value):
        index = self.getHash(key)
        for i, (k, v) in enumerate(self.table[index]):
            #check if the key is already present
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get_value(self, key):
        index = self.getHash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete_key(self, key):
        index = self.getHash(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False
    
    def convert_str_to_int(self,key):
        return sum(ord(c) for c in key)
    
hash = HashWithChaining(5)
hash.insert("name","sahithi")
hash.insert("country","india")
print(hash.get_value("name"))
hash.delete_key("country")
print(hash.get_value("country"))