# Modify the code above to correct the table alignment 
# (แก้ไขโค้ดข้างต้นเพื่อให้ตารางเรียงตรงกันอย่างสวยงาม), as shown in the example below.

# Notes: you may assume (สมมติเอาว่า) that students' names will always be at most 9 characters

name1 = input("Enter name #1: ")
gpa1 = float(input("Enter GPA #1: "))
name2 = input("Enter name #2: ")
gpa2 = float(input("Enter GPA #2: "))

print(f"+-----------+-------+")
print(f"|   Name    |  GPA  |")
print(f"+-----------+-------+")
print(f"| {name1:<9} | {gpa1:<4.2f}  |")
print(f"| {name2:<9} | {gpa2:<4.2f}  |")
print(f"+-----------+-------+")