'''
Write a program that, after taking 3 numbers in input (a, b, c),
prints if the quadratic equation a x2 + b x + c = 0
built with those numbers has
- zero real solutions,
- two coincident solutions
- two real and different solutions
'''
a = int(input("insert value a: "))
b = int(input("insert value b: "))
c = int(input("insert value c: "))
print("The quadratic function is", a, "x^2 +", b, "x +",c,"= 0")
delta = b**2 - 4*a*c
if delta < 0:
    print("The equation has zero real solutions")
elif delta == 0:
    print("The equation has two coincident solutions")
else:
    print("The equation has two real and different solutions")