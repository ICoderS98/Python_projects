#Dice a roll
import random
print(" press 1 to dice a roll ")
print(" press 0 to exit ")
choice = int(input("Enter your choice: "))
while(choice == 1):
    num = random.randint(1,6)
    if num==1:
        print("_________________")
        print("                 ")
        print("       0         ")
        print("                 ")
        print("                 ")
        print("_________________")
    elif num==2:
        print("_________________")
        print("                 ")
        print("      0  0         ")
        print("                 ")
        print("                 ")
        print("_________________")
    elif num==3:
        print("_________________")
        print("                 ")
        print("     0 0 0        ")
        print("                 ")
        print("                 ")
        print("_________________")
    elif num==4:
        print("_________________")
        print("                 ")
        print("     0 0 0         ")
        print("       0         ")
        print("                 ")
        print("_________________")
    elif num==5:
        print("_________________")
        print("                 ")
        print("     0 0 0       ")
        print("      0 0        ")
        print("                 ")
        print("_________________")
    elif num==6:
        print("_________________")
        print("                 ")
        print("     0 0 0       ")
        print("     0 0 0        ")
        print("                 ")
        print("_________________")
    choice = int(input("Enter your choice: "))
    if choice == 0:
        exit()
