import random
all_num = (0,1,2,3,4,5,6,7,8,9,"?","!","@","#","$","%","&","~","=","+")
all_letters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

while True:
    try:
        length = input("I'm going to make a password for you.  How long would you like it to be?: ")
        length = int(length)
        if length < 6:
            print("6 minimum characters required for a safe password.")
            print()
            continue
        while True:
            letters = input("How many letters would you like in your password?: ")
            print()
            letters = int(letters)
            if letters == length or letters == 0:
                print("There must be at least 1 letter and 1 non-letter in each password.")
                print()
                continue
            else:
                break
    except ValueError:
            print("Invalid Input.")
            print("Restarting password creation...")
            print()
            continue
    password = []
    while length > 0:
        if letters == 0:
            new_character = all_num[random.randrange(20)]
            password.append(str(new_character))
            length -=1
        else:
            cap = random.randrange(2)
            if cap == 1:
                new_character = all_letters[random.randrange(26)]
                password.append(new_character.upper())
                length -=1
                letters -=1
            else:
                new_character = all_letters[random.randrange(26)]
                password.append(str(new_character))
                length -=1
                letters -=1
    random.shuffle(password)
    print('Here is your new password: ', "".join(password))
    
    while True:
        answer = input('Would you like to run again for another password? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        print("Restarting password creation...")
        print()
        continue
    else:
        print('Goodbye')
        break

