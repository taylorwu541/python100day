print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Your bill is ${bill}")
    elif 12 <= age <18: 
        bill = 7
        print(f"Your bill is ${bill}")
    else:
        bill = 12
        print(f"Your bill is ${bill}")

    pohot = input("Do you want take photos? Y or N.")
    if pohot == "Y":
            bill += 3
            print(f"Your total bill is ${bill}")
    else:
            print(f"Your total bill is ${bill}")

else :
    print("Sorry,You have to grow taller before you can ride.")
    
