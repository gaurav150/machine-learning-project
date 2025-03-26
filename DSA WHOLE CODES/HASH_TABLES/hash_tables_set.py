class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        hash = 0
        for letter in key:
            hash = (hash + ord(letter) * 23) % len(self.data_map)
        return hash
    
    def print_table(self):
        for i , val in enumerate(self.data_map):
            print(i,":", val)
        
    def set(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

my_hash_table = HashTable()

my_hash_table.set('grapes', 10000)
my_hash_table.set('apples', 54)
my_hash_table.set('oranges', 2)
my_hash_table.set('bananas', 10)
my_hash_table.set('kiwi', 100)


my_hash_table.print_table()
