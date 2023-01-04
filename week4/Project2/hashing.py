class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size
    def hashfunction(self,key):
        keystr = str(key)
        hashVal = 0
        for ch in keystr:
            hashVal += ord(ch)

        return (hashVal*len(keystr)) % self.size
    def rehash(self,key):
        keystr = str(key)
        hashVal = 0
        for ch in keystr:
            hashVal += ord(ch)

        return (hashVal*len(keystr)) // self.size

    def put(self,key,data):
        self[key].append(data)

    def get(self,key):
        return key % len(self)

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        index = hash(key) % len(self)
        self.data[index] = data



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


# Store remaining input data
# print the slot values
# print the data values
# print the value for key 52