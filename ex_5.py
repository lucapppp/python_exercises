'''
Write a program that reads the grade (0-100) of a student, then prints out:
· "A" if it is greater than or equal to 90,
· "B" if its between 89 - 80,
· "C" if its between 79 - 60,
· "D" if its between 59 - 40,
· "F" otherwise.
'''
grade = int(input("Insert your grade: "))
if grade >= 90:
    print("A")
elif 80 <= grade <= 89:
    print("B")
elif 79 <= grade <= 60:
    print("C")
elif 59 <= grade <= 40:
    print("D")
else:
    print("F")