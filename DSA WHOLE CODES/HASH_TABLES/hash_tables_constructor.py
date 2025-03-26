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
        

my_hash_table = HashTable()

my_hash_table.print_table()
