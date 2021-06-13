from border_class import border

def Info_slide():
    break_loop = False
    print("\nInformation about encryption")
    with open("info_slide.txt", "r") as questions:
        question1 = ""
        question2 = ""
        question3 = ""
        question4 = ""
        question5 = ""
        for position, line in enumerate(questions):
            if position == 0:
                question1 += line
            elif position == 4: 
                question2 += line
            elif position == 9: 
                question3 += line
            elif position == 17: 
                question4 += line
            elif position == 23:    
                question5 += line
    while True:
        while True:
            with open("info_slide.txt", "r") as text_file:
                description = ""
                text_list = []
                for x in range(31,43):
                    text_list.append(x)
                for position, line in enumerate(text_file):
                    if position in text_list:
                        description += line
                description1 = border(description, 70)
                description1.create_border()
            correct_answer = [1,2,3,4,5]
            try:
                user_input = int(input("What is your choice? [1-5]: "))
                if user_input in correct_answer:
                    break
                else:
                    print("That is not an answer.")    
            except ValueError:
                print("That is not an answer.")

        if user_input == 1:
            with open("info_slide.txt", "r") as text_file:
                description = ""
                text_list = []
                for x in range(0,3):
                    text_list.append(x)
                for position, line in enumerate(text_file):
                    if position in text_list:
                        description += line
                description1 = border(description, 70)
                description1.create_border()
        elif user_input == 2:
            with open("info_slide.txt", "r") as text_file:
                description = ""
                text_list = []
                for x in range(4,8):
                    text_list.append(x)
                for position, line in enumerate(text_file):
                    if position in text_list:
                        description += line
                description2 = border(description, 70)
                description2.create_border()
        elif user_input == 3:
            with open("info_slide.txt", "r") as text_file:
                description = ""
                text_list = []
                for x in range(9,16):
                    text_list.append(x)
                for position, line in enumerate(text_file):
                    if position in text_list:
                        description += line
                description3 = border(description, 70)
                description3.create_border()
        elif user_input == 4:
            with open("info_slide.txt", "r") as text_file:
                description = ""
                text_list = []
                for x in range(17,22):
                    text_list.append(x)
                for position, line in enumerate(text_file):
                    if position in text_list:
                        description += line
                description4 = border(description, 70)
                description4.create_border()
        elif user_input == 5:
            with open("info_slide.txt", "r") as text_file:
                description = ""
                text_list = []
                for x in range(24,29):
                    text_list.append(x)
                for position, line in enumerate(text_file):
                    if position in text_list:
                        description += line
                description5 = border(description, 70)
                description5.create_border()
        while True:
            continue_search = input("Do you want to continue [Y/N]: ").lower()
            if continue_search == "y":
                break
            elif continue_search == "n":
                break_loop = True
                break
            else:
                print("That's not an answer.")

        if break_loop == True:
            break