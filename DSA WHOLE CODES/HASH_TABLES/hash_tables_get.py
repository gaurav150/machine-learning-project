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

    def get(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]          if i[0] == key:
        return None

my_hash_table = HashTable()

my_hash_table.set('grapes', 10000)
my_hash_table.set('apples', 54)
my_hash_table.set('oranges', 2)
my_hash_table.set('bananas', 10)
my_hash_table.set('kiwi', 100)

print(my_hash_table.get('grapes'))
print(my_hash_table.get('apples'))
print(my_hash_table.get('oranges'))
print(my_hash_table.get('bananas'))
print(my_hash_table.get('kiwi'))


my_hash_table.print_table()
