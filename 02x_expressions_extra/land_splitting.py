# A landlord owns a piece of rectangle-shaped land of size width x length sq.m. 
# He wants to split the land into pieces of 100 sq.m each for sale. 
# The remaining piece of land, which is smaller than 100 sq.m, will not be sold.

# Your task
# Write a program that reads two values: width and length, respectively. The program then outputs the number of 100-sq.m pieces he will have available for sale.

width = int(input("Enter width: "))
height = int(input("Enter length: "))
x = width * height
num = int(x / 100)
print(f"The landlord will have {num} of land available for sale.")