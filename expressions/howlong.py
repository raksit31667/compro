# Write a program that takes the number of seconds passed (จำนวนวินาทีที่ผ่านไป)
#  and displays the same amount of time in hours, minutes, and seconds.

seconds = int(input("How many seconds have passed? "))
hours = int(seconds / 3600)
seconds -= hours*3600
minutes = int(seconds / 60)
seconds -= minutes*60
print(f"{hours} hour(s) {minutes} minute(s) and {seconds} second(s) have passed.")