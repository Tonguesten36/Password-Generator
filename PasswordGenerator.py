import random

print("------------[PASSWORD GENERATOR]------------")
print("------------[MADE BY TONGUESTEN]------------")

while True:
    operation = input("Do you want to generate a new password?[y/n]: ")

    if operation == "y" or operation == "Y":
        password = []

        while True:
            try:
                length = int(input("Password length: "))
                if length > 0:
                    break
            except ValueError:
                print("Must be an integer")

        # Generating a new password
        for i in range(0, length, 1):
            randomCharacterType = random.randint(0, 3)
            
            if randomCharacterType == 0:
                password.append(chr(random.randint(97,122)))
            elif randomCharacterType == 1:
                password.append(chr(random.randint(65, 90)))
            elif randomCharacterType == 2:
                password.append(chr(random.randint(48, 57)))
            else:
                password.append(chr(random.randint(33, 38)))

        print("".join(password))  
    elif operation == "n" or operation == "N":
        exit()
    else:
        print("Please type again")
