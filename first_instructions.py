print("Hello World!")
#functions are called with funtction_name(arg1, arg2, ...)
#there are even functions with no variables
#variables are slots of memory
name = "Luca"
print("Hi", name, "!")
#variables can be riassigned
name2 = "Loris"
name = name2
print("Hi", name)
#it can even change type of variable
name = 4.23 #now it's a float
#i can specify a variable by saying the value. It means to cast a value
number = int(name)
#if i dont remember the type of a varibale i say type(variable_name)
print(type(number))
#constants are usefull to store informations
#i need a location where i can store it and it never will change
CONSTANT = 24 #i store it using capital letter
print(CONSTANT)
#how can i use input from the user?
name = input("Please insert your name: ") #the terminal prints the text i wrote in input. I can also just write input()
print(name)
#i can specify what the input will be by casting it
number = int(input("Insert an integer if u dont wanna have an error: ")) #if i input another variable from what i cast it gives me error
#operations
2 + 2
#divisions
5 / 2 #this is a simple division
5 % 2 #this is modulus, i get what id get as rest of the division
5 // 2 #this is the floor division (just the integer part)
#exponent 
2 ** 2
#operations follow the usual rules of algebra, so first i say exp, then moltiplication ecc... ofc parenthesis come first
#i can make operations with variables
a = 5
b = 7
print(a/b)
#arithmetics functions
#absolute function abs()  is the absolute value
abs(-5)
#round() rounds it up to the next integer
round(3.1) #gives 4
#min(var 1, var 2) takes a list of values and gives me the minimum one
min(2, 3, number, -2)
#max same, just for the maximum
