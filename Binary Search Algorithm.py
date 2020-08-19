import random
import sys
def script():
    registry = random.randint(100, 2000)*99
    print("Welcome to the Intergalactic Banking Clan Account Directory.")
    print()
    print("Now searching Registry #", registry)
    print()
    print("Standard systems have Accounts labled: 0-100")
    print()
    runtime = 50
    the_list = []
    chance = random.randint(0,1)
    while runtime > 0:
        if chance == 0:
            the_list.append(random.randint(0,50)*2)
        else:
            the_list.append(random.randint(0,50)*2-1)
        runtime -= 1
    while True:
        try:
            print("What Account number are you looking for?")
            search = input("Please input Account number (cap is 100): ")
            if int(search) in the_list:
                print()
                print("Account located.")
                print("Location of the Account within the Registry: ", "Vault", the_list.index(int(search)))
            else:
                print()
                print("Account not found, we cannot locate the Account you looking for in our system.")
        except ValueError:
            print("Invalid Input.")
            print()
            continue
        while True:
            print()
            answer = input("Would you like to look for another Account in THIS system? (y/n): ")
            answer = answer.lower()
            print()
            if answer == "y" or answer == "yes":
                break
            elif answer == "n" or answer == "no":
                print("Logging out of system...")
                print()
                break
            else:
                print("Invalid Input.")
        if answer == "n" or answer == "no":
            break
    while True:
        restart = input("Would you like to find another Account in a DIFFERENT system? (y/n): ")
        restart = restart.lower()
        print()
        if restart == "yes" or restart == "y":
            script()
        elif restart == "n" or restart == "no":
            print("Script terminating. Goodbye.")
            sys.exit()
        else:
            print("Invalid Input.")
            continue
script()
