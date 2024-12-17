def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
   
    roll_numbers = [101, 102, 105, 110, 115, 120, 125, 130, 135]

    print("Roll numbers of students who attended the training program:")
    print(roll_numbers)
  
    target_roll = int(input("Enter roll number to search: "))

    binary_result = binary_search(roll_numbers, target_roll)
    if binary_result != -1:
        print(f"Binary Search: Roll number {target_roll} found at index {binary_result}.")
    else:
        print(f"Binary Search: Roll number {target_roll} not found.")

if __name__ == "__main__":
    main()

