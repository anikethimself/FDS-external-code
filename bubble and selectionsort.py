def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
   
                arr[j], arr[j+1] = arr[j+1], arr[j]

def display_top_scores(arr, top_n=5):
    print(f"\nTop {top_n} first year percentages:")
  
    for i in range(min(top_n, len(arr))):
        print(f"{i+1}. {arr[-(i+1)]:.2f}")  

def main():
    
    first_year_percentages = [65.5, 72.3, 85.7, 91.2, 63.4, 78.9, 56.3, 99.0, 80.6, 70.1]
    selection_sort(first_year_percentages)
    print("\nSorted first year percentages using Selection Sort:")
    print(first_year_percentages)
    
    first_year_percentages = [65.5, 72.3, 85.7, 91.2, 63.4, 78.9, 56.3, 99.0, 80.6, 70.1]
    bubble_sort(first_year_percentages)
    print("\nSorted first year percentages using Bubble Sort:")
    print(first_year_percentages)

    display_top_scores(first_year_percentages)

if __name__ == "__main__":
    main()

