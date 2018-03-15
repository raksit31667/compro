# Your best friend needs to know how profitable it would be 
# to put his money in a savings account. 
# 
# Help your friend by writing a Python program to compute the amounts of money
# he would have in his account after certain numbers of years have passed.

# Requirements
# Your program must take two inputs: 
# (1) the initial amount in Baht, and 
# (2) the annual interest rate in percent. 
# Both numbers can be any non-negative numbers that can contain fraction.

# There must be four lines of output to report the amounts of money 
# in the account after 1, 5, 10, and 20 years have passed, respectively.

# The output amounts must be displayed with 2 decimal places.

amount = float(input("Enter initial amount in Baht: "))
rate = float(input("Enter interest rate in percent: "))
sum = amount*((100 + rate)/100)**1
print(f"Total amount after 1 year is {sum:<.2f} Baht.")
sum = amount*((100 + rate)/100)**5
print(f"Total amount after 5 years is {sum:<.2f} Baht.")
sum = amount*((100 + rate)/100)**10
print(f"Total amount after 10 years is {sum:<.2f} Baht.")
sum = amount*((100 + rate)/100)**20
print(f"Total amount after 20 years is {sum:<.2f} Baht.")