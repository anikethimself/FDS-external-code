def sentinel_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1

    last = arr[-1]
    arr[-1] = target
   
    i = 0
    while arr[i] != target:
        i += 1

    arr[-1] = last
    
    if i < n - 1 or arr[-1] == target:
        return i 
    else:
        return -1  

def main():
    roll_numbers = [101, 102, 103, 104, 105, 106, 107]

    import random
    random.shuffle(roll_numbers)

    print("Roll numbers of students who attended the training program:", roll_numbers)
    target_roll_number = int(input("Enter the roll number to search: "))
            
	#search using sentinel search
    index_sentinel = sentinel_search(roll_numbers.copy(), target_roll_number)  
    if index_sentinel != -1:
        print(f"Sentinel Search: Roll number {target_roll_number} found at index {index_sentinel}.")
    else:
        print(f"Sentinel Search: Roll number {target_roll_number} not found.")

if __name__ == "__main__":
    main()

