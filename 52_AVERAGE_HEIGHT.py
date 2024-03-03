# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total_height = 0
number_of_students = 0

for one_student in student_heights :
  total_height += one_student
  number_of_students += 1
average_height = round(total_height / number_of_students)
print("total height =",total_height)
print("number of students =",number_of_students)
print("average height =",average_height)
