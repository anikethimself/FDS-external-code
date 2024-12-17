""" 
Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students in the class. Write functions to compute following: 
a) The average score of class 
b) Highest score and lowest score of class 
c) Count of students who were absent for the test 
d) Display mark with highest frequency 
"""

def average(marks):
    total_marks = sum(marks)
    average = total_marks / len(marks)
    return average

def find_highest_lowest(marks):
    highest = max(marks)
    lowest = min(marks)
    return highest, lowest

def absent(students):
    absent_count = students.count('A')
    return absent_count

def highest_frequency(marks):
    frequency_dict = {}
    for mark in marks:
        if mark in frequency_dict:
            frequency_dict[mark] += 1
        else:
            frequency_dict[mark] = 1

    max_frequency = max(frequency_dict.values())
    most_frequent_marks = [mark for mark, count in frequency_dict.items() if count == max_frequency]
    
    return most_frequent_marks, max_frequency

N = int(input("Enter the number of students: "))
marks = []
students = []  

for i in range(N):
    mark = input(f"Enter the marks for student {i+1} (Type 'A' if the student is absent): ")
    students.append(mark) 
    if mark.upper() == 'A': 
        marks.append(0) 
    else:
        marks.append(int(mark))

average_score = average(marks)
print("The average score of the class is: %.2f" % average_score)

highest, lowest = find_highest_lowest(marks)
print("The highest score in the class is:", highest)
print("The lowest score in the class is:", lowest)

absent_count = absent(students)
print("The total number of absent students is:", absent_count)

most_frequent_marks, frequency = highest_frequency(marks)
print("The mark(s) with the highest frequency is/are:", most_frequent_marks)
