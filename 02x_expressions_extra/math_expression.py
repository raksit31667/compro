# Write a program that reads two variables, x and y from the user. 
# The program then evaluates and shows the value of the following 
# mathematical expression with five decimal places:

x = int(input("Enter x: "))
y = int(input("Enter y: "))
result = ((x-y)/(x+y)) * (3.14 / (0.15 + (y/x)))
print(f"The result is {result:<10.5}")
