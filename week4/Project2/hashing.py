class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        return key % self.size

    def rehash(self,key):
        return key // self.size
        
    def put(self,key,data):
        hashValue = self.hashfunction(key)
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            hashValue = self.rehash(key)
            if self.slots[hashValue] == None:
                self.slots[hashValue] = key
                self.data[hashValue] = data
            else:
                print("Error: Collision")

    def get(self,key):
        hashValue = self.hashfunction(key)
        if self.slots[hashValue] == key:
            return self.data[hashValue]
        else:
            hashValue = self.rehash(key)
            if self.slots[hashValue] == key:
                return self.data[hashValue]
            return None

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)



H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

print(H.slots)
print(H.data)
print(H[52])

# Store remaining input data
# print the slot values
# print the data values
# print the value for key 52