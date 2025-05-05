class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert_without_replacement(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = key
                return
        print("Table full!")

    def insert_with_replacement(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = key
        else:
            existing_key = self.table[index]
            if self.hash_function(existing_key) != index:
                # Replace and reinsert the existing key
                self.table[index] = key
                self.insert_without_replacement(existing_key)
            else:
                self.insert_without_replacement(key)

    def display(self):
        print("Hash Table:")
        for i in range(self.size):
            print(f"{i}: {self.table[i]}")


# Example usage
print("Without Replacement:")
ht1 = HashTable(7)
ht1.insert_without_replacement(10)
ht1.insert_without_replacement(3)
ht1.insert_without_replacement(17)
ht1.insert_without_replacement(24)
ht1.display()

print("\nWith Replacement:")
ht2 = HashTable(7)
ht2.insert_with_replacement(10)
ht2.insert_with_replacement(3)
ht2.insert_with_replacement(17)
ht2.insert_with_replacement(24)
ht2.display()
