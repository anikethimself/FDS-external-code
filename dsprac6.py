"""
Write a python program to store roll numbers of student array who attended training program in sorted order. 
Write function for searching whether particular student attended training program or not, using Binary search.
"""
def binary_search(arr,target):
    n=len(arr)
    low=0
    high=n-1
    
    while low<=high:
        mid=(low+high)//2
        
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1 
        else:
            high=mid-1 
    return -1 
    
def main():
    roll_no=[101,102,103,104,105,106,107]
    
    roll_no.sort()
    print("The roll no who attended the training program:",roll_no)
    target_roll=int(input("Enter the roll no to search:"))
    
    index=binary_search(roll_no,target_roll)
    if index!=-1:
        print(f"The roll no. {target_roll} is found at index {index}. ")
    else:
        print("not found!!!!!!!!!")
if __name__=="__main__":
    main()
