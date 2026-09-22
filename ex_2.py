'''
Write a program that, after taking a number lower than 10 in input,
prints if the number is a multiple of 2 or of 3. If the number is
higher than 10, it prints an error
'''
n1 = int(input("Insert a number lower than 10: "))
if n1 == 10:
    print("The number is equal to 10")
elif n1 > 10:
    print("The number is greater than 10")
else:
    if n1 % 2 == 0 or n1 % 3 == 0:
        print("It is a multiple of 2 or 3")
    else:
        print("It's not")