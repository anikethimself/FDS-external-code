def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

def main():
    roll_numbers = [101, 102, 103, 104, 105, 106, 107]

    import random
    random.shuffle(roll_numbers)

    print("Roll numbers of students who attended the training program:", roll_numbers)
    target_roll_number = int(input("Enter the roll number to search: "))
    
	#search using sentinel search
    index_linear = linear_search(roll_numbers, target_roll_number)
    if index_linear != -1:
        print(f"Linear Search: Roll number {target_roll_number} found at index {index_linear}.")
    else:
        print(f"Linear Search: Roll number {target_roll_number} not found.")

if __name__ == "__main__":
    main()

