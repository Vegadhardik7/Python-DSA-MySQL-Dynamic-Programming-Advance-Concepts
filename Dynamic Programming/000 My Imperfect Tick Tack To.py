print("Tick Tack To")


'''
    _1_|_2_|_3_
    _4_|_5_|_6_    
     7 | 8 | 9 

number_of_spaces  = [1,2,3,4,5,6,7,8,9]
number_of_players = [0,1] # 0: Computer, 1: Human
all_possible_wins = [123,456,789,147,258,369,159,357]

if i entered al ready removed number print "this number is already removed remaining number []" 

'''
import random         # import random

toss = input("press * : ")  # Do toss

toss_result = None          # Bcz result not yet decided

number_of_spaces  = [1,2,3,4,5,6,7,8,9]       # Number of box to fill

all_possible_wins_final = [123,456,789,147,258,369,159,357] # Number of possible wins

# to make values a string that int, split by every 3rd element
# com = 0
# hum = 0

computer = []      # list which store space for computer
human  = []        # list which store space for humans

if toss == '*':      # * to do toss
    random.random()  # Gives you a number BETWEEN 0 and 1 as a float
    toss_result = round(random.random())  # Gives you a number EITHER 0 and 1

    if toss_result == 0:     # if toss_result == 0: Computer will choose
        print("Toss Won By Computer")
        while True:

            value1 = random.choice(number_of_spaces)   # Computer choose random value
            # com+=value1
            computer.append(str(value1)) # making it into string so sorting and splitting would be easy
            print("Computer Selected:", computer)  # Print computer
            number_of_spaces.remove(value1)        # remove it from number_of_spaces
            print("Number of values left:",number_of_spaces) # printing remaining space after removing value

            if len(computer)%3 == 0:
                new_computer = sorted(computer)
                new_com = ''.join(new_computer)
                com = int(new_com)

                if com in all_possible_wins_final:
                    print("Computer Won")
                    exit()
                else:
                    computer.append(str(value1))

            value2 = int(input("Enter the number between 1-9: ")) # Human Turn
            if 0 < value2 <= 9:       # value should be between 1-9
                human.append(str(value2))  # making it into string so sorting and splitting would be easy
                print("Human Selected: ",human)
                number_of_spaces.remove(value2)
            else:
                print("Values should be between 1-9")
            print("Number of Spaces Left:", number_of_spaces)

            if len(human)%3 == 0:
                new_human = sorted(human)
                new_hum = ''.join(new_human)
                com = int(new_hum)

                if com in all_possible_wins_final:
                    print("Human Won")
                    exit()
                else:
                    human.append(str(value2))

    else:
        print("Toss Won By Human")
        while True:

            value3 = int(input("Enter the number between 1-9: "))
            if 0 < value3 <= 9:
                human.append(str(value3))
                print("Human Selected: ",human)
                number_of_spaces.remove(value3)
            else:
                print("Values should be between 1-9")
            print("Number of Spaces Left:" ,number_of_spaces)

            if len(human)%3 == 0:
                new_human = sorted(human)
                new_hum = ''.join(new_human)
                com = int(new_hum)

                if com in all_possible_wins_final:
                    print("Human Won")
                    exit()
                else:
                    human.append(str(value3))

            value4 = random.choice(number_of_spaces)
            computer.append(str(value4))
            print("Computer Selected: ",computer)
            number_of_spaces.remove(value4)
            print("Number of Spaces Left:", number_of_spaces)

            if len(computer)%3 == 0:
                new_computer = sorted(computer)
                new_com = ''.join(new_computer)
                com = int(new_com)

                if com in all_possible_wins_final:
                    print("Computer Won")
                    exit()
                else:
                    computer.append(str(value4))

else:
    print("You exited the game")



