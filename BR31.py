import random as rand
user = 0    # Get User Number
default = 1 # Sum Game Number of last
WIN = 30    # BR31 rules one: who enter 31 is defeat

# Set Error 1: Over or Under enter Number
class ErrorNum(Exception):
    def __str__(ern):
        return("Wrong Number")
    
# Set Error 2: Variable is not type Integer
class WrongEnter(Exception):
    def __str__(wen):
        return ("Please Enter Number")

# Organize Computer Win with Switch~case
def Win_Com_Num(num):
    return {
        num <= 26 and num >= 24: 1,
        28 : 2,
        27 : 3,
        29 : 1
    }. get(num, 1)

# Start Game (__main__)
print("Welcome to BR31 game!")
while True:
    # Check and get User Number
    try:
        user = input("Input Number : ")
        user_num = user.split(" ")
        # if user enter wrong Number
        if len(user_num) > 3 or int(user_num[-1]) <= default or int(user_num[-1]) > default + 3:
            raise ErrorNum()
    except ErrorNum as e:
        print(e)
        continue
    except ValueError:
        print(WrongEnter())
        continue 

    # Save last of User number
    default = int(user_num[-1])

    # Check Game rules by User
    if default >= 31:
        print("Over Number 31")
        print("You Lose!")
        break

    # Computer set Number
    Com_Rand_Set = rand.randint(1, 3)

    # Can win Computer (1)
    if default >= 24 and default <= 29:
        Com_Rand_Set = Win_Com_Num(default)
    Com_def = Com_Rand_Set + default

    # Can win Computer (2)
    if Com_def == 27:
        Com_Rand_Set = 1

    # Check Game rules by Computer
    if Com_def >= 31 or default == WIN:
        print("Computer Over Number 31")
        print("You Win!")
        break

    # Print Computer Number
    if Com_def <= WIN:
        print("Computer Number: ", end='')
        for cmn in range(Com_Rand_Set):
            print((cmn + 1) + default, end=' ')
            # Can win Computer (3)
            if (cmn + 1) + default == WIN:
                Com_def = WIN
                break
    print(" ")

    # Save last of Computer Number
    default = Com_def
