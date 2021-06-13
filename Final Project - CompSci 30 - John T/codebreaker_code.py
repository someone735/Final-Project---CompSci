import random
from border_class import border


def CodeBreaker():
    begin_game = True
    with open("codebreaker_text.txt", "r") as question:
        question_text = ""
        question_list = []
        for x in range(0,12):
            question_list.append(x)
        for position, line in enumerate(question):
            if position in question_list:
                question_text += line
    display_text = border(question_text,75)
    display_text.create_border()

    while True:
        while True:
            start_game = input("New Game [Y/N]: ").lower()
            if start_game == "y":
                break
            elif start_game == "n":
                begin_game = False
                break
            else: 
                print("That's not an answer.")
            
        if begin_game == False:
            print("Thanks for playing")
            break

        if begin_game == True:
            randomized_num = random.randint(1000,10000)
            randomized_num_string = str(randomized_num)
            randomized_num_list = randomized_num_string.split()
            input_num = []
            correcting_list = []
            for x in range(7):
                input_num.append("####")
                correcting_list.append("####")
            correct_guess = False
            for y in range(8):
                for i in range(len(input_num)):
                    print("|" + str(input_num[i])+ "|    |" + str(correcting_list[i]) + "|")
                if y == 7:
                    break
                while True:
                    try:
                        user_guess = input("What is your guess? ")
                        user_guess_len = user_guess
                        user_guess = int(user_guess)
                        if len(user_guess_len) == 4:
                            break
                        else:
                            print("That's not a four digit number.")
                    except ValueError:
                        print("That's not a number.")
                if user_guess == randomized_num:
                    print("You have cracked the code. " +str(user_guess) + " is the correct number.")
                    correct_guess = True
                    break
                else:
                    input_num[y] = user_guess
                    user_guess = str(user_guess).split()
                    result_output = ""
                    for z in range(4):
                        if user_guess[0][z] == randomized_num_list[0][z]:
                            result_output += str(user_guess[0][z])
                        
                        elif user_guess[0][z] in randomized_num_string:
                            result_output += "Y"

                        else:
                            result_output += "X"
                    correcting_list[y] = result_output 
            if correct_guess == False:
                print("You couldn't crack the code. The code was " + str(randomized_num))
            