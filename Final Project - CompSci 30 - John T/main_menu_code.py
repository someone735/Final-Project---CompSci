from codebreaker_code import CodeBreaker
from info_slide_code import Info_slide
from border_class import border
from decrypt_class import decrypt
from encrypt_class import encrypt

with open("main_menu.txt", "r") as title:
    title_list = []
    title_display = ""
    for x in range(12,25):
        title_list.append(x)
    for position, line in enumerate(title):
        if position in title_list:
            title_display += line
    print("\n"+ title_display + "\n")
 
while True:
    with open("main_menu.txt", "r") as start:
        main_text = ""
        main_list = []
        for x in range(0,11):
            main_list.append(x)
        for position, line in enumerate(start):
            if position in main_list:
                main_text += line
    start_text = border(main_text,30)
    start_text.create_border()

    while True:
        choice_list = [1,2,3,4,5]
        try:
            choice = int(input("What is your selection? [1-5]: "))
            if choice in choice_list:
                break
            else:
                print("That is not an answer.")
        except ValueError:
            print("That is not an number.")
    
    if choice == 1:
        break_loop = False
        with open("decrypt_and_encrypt.txt", "r") as encryption_question:
            question_text = ""
            question_list = []
            for x in range(0,4):
                question_list.append(x)
            for position, line in enumerate(encryption_question):
                if position in question_list:
                    question_text += line
        encryption_display = border(question_text,60)
        encryption_display.create_border()
        while True:
            input_text = input("Input text here: ")
            encrypted_string = encrypt(input_text)
            print("Encrypted String: " + encrypted_string.encryptString())
            while True:
                continue_var = input("Do you encrypt another string? [Y/N]: ").lower()
                if continue_var == "y":
                    break
                elif continue_var == "n":
                    print("Hope to see you again.")
                    break_loop = True
                    break
                else:
                    print("That is not an answer.")
            if break_loop == True:
                break
    elif choice == 2:
        break_loop = False
        with open("decrypt_and_encrypt.txt", "r") as decryption_question:
            question_text = ""
            question_list = []
            for x in range(6,10):
                question_list.append(x)
            for position, line in enumerate(decryption_question):
                if position in question_list:
                    question_text += line
        decryption_display = border(question_text,60)
        decryption_display.create_border()
        while True:
            input_text = input("Input text here: ")
            decrypted_string = decrypt(input_text)
            print("Decrypted String: " + decrypted_string.decryptString())
            while True:
                continue_var = input("Do you decrypt another string? [Y/N]: ").lower()
                if continue_var == "y":
                    break
                elif continue_var == "n":
                    print("Hope to see you again.")
                    break_loop = True
                    break
                else:
                    print("That is not an answer.")
            if break_loop == True:
                break

    elif choice == 3:
        Info_slide()

    elif choice == 4:
        CodeBreaker()

    elif choice == 5:
        end_text = border("Thank you for using The Secrets in Plaintext", 50)
        end_text.create_border()
        break