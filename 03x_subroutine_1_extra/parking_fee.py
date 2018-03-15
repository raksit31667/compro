# At an airport, the parking rate (อัตราค่าจอดรถ) is 25 baht/hour, 
# where the fraction of an hour is rounded to a whole hour (เศษของชั่วโมงคิดเป็น 1 ชั่วโมง).

# Write a program that takes the number of minutes and computes the total parking fee (ค่าจอดรถ).

import math
minutes = int(input("Enter parking time in minutes: "))
fee = int(math.ceil(minutes/60)) * 25
print(f"Parking fee is {fee} baht.")