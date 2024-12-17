cricket=["Aniket","Vinay","Pranav","Rohit"]
football=["Aniket","ishwar","vishal","Amit","Pranav"]
badminton=["vishal","Vinay","sahil","Rohit"]

def common(a, b):
    return [x for x in a if x in b]
def either(a, b):
	return [x for x in (a+b) if (x in a or x in b) and x not in common(a,b)]
def neither(a,b,allstu):
	return [x for x in allstu if x not in (a+b)]
def exceptbadminton(cri,ft,bad):
	cricketandfootball=common(cri,ft)
	return [x for x in cricketandfootball if x not in bad]
    
allstu = list(set(cricket+football+badminton))
c=common(cricket,badminton)
e=either(cricket,badminton)
n=neither(cricket,badminton,allstu)
ex=exceptbadminton(cricket,football,badminton)

print("List of all students:",allstu)
print("List of students who play both cricket and badminton is:",c)
print("List of students who play either cricket or badminton but not both is:",e)
print("Number of students who play neither cricket nor badminton is:",n)
print("Number of students who play cricket and football but not badminton is:",ex)

