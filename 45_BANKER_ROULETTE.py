names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random

'''
random_name = random.randint(0,4)
paylist = (names[random_name])

print(f"{paylist} is going to buy the meal today!")
'''

name_item = len(names)
random_name = random.randint(0,name_item-1)
paylist = (names[random_name])

print(f"{paylist} is going to buy the meal today!")
