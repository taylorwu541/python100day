print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
allinone = name1 + name2
twoname = allinone.lower()
count1 = twoname.count("t")
count2 = twoname.count("r")
count3 = twoname.count("u")
count4 = twoname.count("e")
true = count1 + count2 +count3 +count4
count5 = twoname.count("l")
count6 = twoname.count("o")
count7 = twoname.count("v")
count8 = twoname.count("e")
love = count5 + count6 +count7 +count8
truelove = str(true) + str(love)

if int(truelove) < 10 or int(truelove) > 90:
  print("Your score is" , truelove + ", you go together like coke and mentos.")

elif 40 < int(truelove) < 50:
  print("Your score is" , truelove +", you are alright together.")

else:
    print("Your score is" , truelove + ".")
