#conditional execution is used to give the the program the ability to make decision
#based on the true or false condition there will be  consequences
#if it's true do this else do that
#2 ways to implement conditinal execution: if-else or if-elif-else
if 5 > 2:
    print("Hi") #remember the indentation. It does everything that is idented after the if
n1 = int(input("Insert the first number: "))
n2 = int(input("Insert the second number: "))
if n1 > n2:
    print("n1 is greater")
elif n1 == n2:
    print("Both number are the same")
else:
    print("n2 is greater")
#but the user is unpredictable so i have to make sure it's an int
#i cast the isnumeric() function. We'll see hot it works later
'''
if n1.isnumeric() and n2.isnumeric():
    if n1 > n2:
        print("n1 is greater")
    elif n1 == n2:
        print("Both number are the same")
    else:
        print("n2 is greater")
else:
    print("U didnt insert a number")
'''
#i can also say the logic operators, like and, or and not
