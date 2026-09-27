'''
Exercise: suppose to design and implement a costumer registration software for a go kart
circuit. The software asks the user to insert her year of birth and responds in different ways:
• If the value inserted is not a number, or if the number is greater than the current year, then print
an error message and exit;
• If the age of the user is < 14 then prints that he is not allowed to register;
• If the age is between >= 14 but < 18 prints that he needs parents authorization;
• If the age is >= 18 allows the registration.
'''

year = int(input("Insert your year of birth: "))
if year > 2026:
    print("ERROR: invalid year")
else:
    if (2026 - year) < 14:
        print("User not allowed to register!")
    elif 14 <= (2026 - year) < 18:
        print("The user needs parents authorization!")
    else:
        print("Registration is allowed")