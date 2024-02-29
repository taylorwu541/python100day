rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_image =[rock,paper,scissors]
print("What do you choose? Type 0 for rock, 1 for paper 2 for scissor.")

import random

player_choose = int(input())
print("Your Choose:")
print(game_image[player_choose])

cp_choose = random.randint(0,2)
print("CP Choose:")
print(game_image[cp_choose])

if player_choose == cp_choose:
    print("It is a draw.")
    
elif 0 < player_choose - cp_choose < 2 or player_choose - cp_choose == "-2" :
    print("You Win!")

else:
    print("You Lose!")
