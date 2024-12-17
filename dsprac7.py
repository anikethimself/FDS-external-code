"""
Write a python program to store roll numbers of student array who attended training program in sorted order.
Write function for searching whether particular student attended training program or not, using Fibonacci search.
"""
def fibonacci_search(arr, x):
    m2 = 0  
    m1 = 1  
    fib_m = m2 + m1  

    n = len(arr)
    offset = -1

    while fib_m < n:
        m2 = m1
        m1 = fib_m
        fib_m = m2 + m1

    while fib_m > 1:
        i = min(offset + m2, n - 1)

        if arr[i] < x:
            fib_m = m1
            m1 = m2
            m2 = fib_m - m1
            offset = i
 
        elif arr[i] > x:
            fib_m = m2
            m1 = m1 - m2
            m2 = fib_m - m1

        else:
            return i

    if m1 and offset + 1 < n and arr[offset + 1] == x:
        return offset + 1

    return -1

def main():
   
    roll_numbers = [101, 102, 105, 110, 115, 120, 125, 130, 135]

    print("Roll numbers of students who attended the training program:")
    print(roll_numbers)

    target_roll = int(input("Enter roll number to search: "))

    fibonacci_result = fibonacci_search(roll_numbers, target_roll)
    if fibonacci_result != -1:
        print(f"Fibonacci Search: Roll number {target_roll} found at index {fibonacci_result}.")
    else:
        print(f"Fibonacci Search: Roll number {target_roll} not found.")

if __name__ == "__main__":
    main()
