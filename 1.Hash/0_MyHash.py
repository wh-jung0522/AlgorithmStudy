# TODO : Make Hash Table
#        input .txt file
#           key value\n ... 

class myHashTable():
    def __init__(self,len=8):
        self.len = len
        self.HashTable = list([[] for i in range(len)])
    def hashFunction(self,key):
        return (int(key.encode().hex())%(self.len))
    def insert(self,key,value):
        self.HashTable[self.hashFunction(key)].append(value)
    def read(self,key,value):
        ReadList = self.HashTable[self.hashFunction(key)]
        for i in range(len(ReadList)):
            if (ReadList[i] == value):
                print(self.hashFunction(key),i)
                return self.hashFunction(key),i
        print("Not Exist\n")
    def print(self):
        print(self.HashTable)

if __name__ == '__main__':
    data = open("1.Hash\hashTest.txt",'r')
    HashTable = myHashTable(4)
    while True:
        line = data.readline()
        if not line: break
        key = line.split(" ")[0]
        value = line.split(" ")[1].strip()
        HashTable.insert(key,value)
    
    HashTable.print()

