target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

total = 0

for even_number in range(2 , target + 1 , 2):
   total += even_number
print(total)
