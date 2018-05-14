class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunc(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size  # linear probing

    def put(self, key, val):
        hashval = self.hashfunc(key, self.size)
        if self.slots[hashval] is None:
            self.slots[hashval] = key
            self.data[hashval] = val
        elif self.slots[hashval] == key:
            self.data[hashval] = val  # replace
        else:
            nextslot = self.rehash(hashval, self.size)
            while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, self.size)
            if self.slots[nextslot] is None:
                self.slots[nextslot] = key
                self.data[nextslot] = val
            else:
                self.data[nextslot] = val  # replace

    def get(self, key):
        pos = self.hashfunc(key, self.size)
        while self.slots[pos] is not None and self.slots[pos] != key:
            pos = self.rehash(pos, self.size)
        if self.slots[pos] is None:
            return None
        else:
            return self.data[pos]

    def loadFactor(self):
        return "{} / {}".format(self.__len__(), self.size)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        return len([x for x in self.slots if x is not None])

    def __contains__(self, key):
        return key in self.slots


def strhash(string1, tablesize):
    sum1 = 0
    for i, ch in enumerate(string1):
        sum1 += ord(ch) * (i + 1)
    return sum1 % tablesize


if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    print(H[20])
    print(H[17])
    H[20] = 'duck'
    print(H[20])
    print(H.data)
    print(len(H))
    print(20 in H)
    print(H.loadFactor())
