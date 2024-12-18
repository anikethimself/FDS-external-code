def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
    return -1

def main():
    roll_no=[101,102,103,104,105,106,107]
    
    import random
    random.shuffle(roll_no)
    print("Roll no. of students who attended the training program:",roll_no)
    
    target_roll=int(input("Enter the roll no to search:"))
    
    index=linear_search(roll_no,target_roll)
    
    if index!=-1:
        print(f"The roll no {target_roll} is found at index{index}")
    else:
        print("the roll no is not found")
    
if __name__=="__main__":
    main()
