'''
Write a program that, after taking two numbers in input, prints if the
first number is higher or lower than the second one
'''
n1 = int(input("Insert the 1st number: "))
n2 = int(input("Insert the 2nd number: "))
if n1 > n2:
    print("n1 is greater")
elif n1 == n2:
    print("The numbers are equivalent")
else:
    print("n2 is greater")