class Linearprob:
    def init(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, phone):
        return int(phone) % self.size

    def insert(self, phone, name):
        index = self.hash_function(phone)
        comp = 1
        while self.table[index] is not None:
            index = (index + 1) % self.size
            comp += 1
        self.table[index] = (phone, name)
        return comp

    def search(self, phone):
        index = self.hash_function(phone)
        comp = 1
        while self.table[index] is not None:
            if self.table[index][0] == phone:
                return comp
            index = (index + 1) % self.size
            comp += 1
        return comp

contacts = {
    "1234": "Alice",
    "5678": "Bob",
    "9101": "Charlie",
    "1121": "David",
    "3141": "Eve",
    "5161": "Frank"
}

size = 7  # Small size to force collisions
linear_table = Linearprob(size)

print("Insert Comparisons:")
for phone, name in contacts.items():
    lp_cmp = linear_table.insert(phone, name)
    print(f"{phone} ({name}): Linear={lp_cmp}")

print("\nSearch Comparisons:")
for phone in contacts.keys():
    lp_cmp = linear_table.search(phone)
    print(f"{phone}: Linear={lp_cmp}")