class Linearprob:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
    
    def hash_function(self,phone):
        return int(phone)%self.size
    
    def insert(self,phone,name):
        index=self.hash_function(phone)
        comp=1
        while self.table[index] is not None:
            index=(index+1)%self.size
            comp+=1
        self.table[index]=(phone,name)
        return comp
    
    def search(self,phone):
        index=self.hash_function(phone)
        comp=1
        while self.table[index] is not None:
            if self.table[index][0]==phone:
                return comp
            index=(index+1)%self.size
            comp+=1
        return comp

contacts={
    "1234":"aniket",
    "5678":"boi",
    "9101":"maba",
    "1121":"heks",
    "3141":"bbfn",
    "5161":"dsdd"
}
size=7
Linear_table=Linearprob(size)

print("Insert comparisons:")
for phone, name in contacts.items():
    lp_cmp=Linear_table.insert(phone,name)
    print(f"{phone} ({name}) : Linear={lp_cmp}")

print("\nsearch comparisons:")
for phone in contacts.keys():
    lp_cmp=Linear_table.search(phone)
    print(f"{phone}: Linear={lp_cmp}")