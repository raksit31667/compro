import math
minutes = int(input("Enter parking time in minutes: "))
fee = int(math.ceil(minutes/60)) * 25
print(f"Parking fee is {fee} baht.")