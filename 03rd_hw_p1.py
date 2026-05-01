
while 1:
    user_name = input("Введіть власне ім'я та прізвище через пробіл: ")

    if (user_name.isspace()):
        print('Your string does not contain any words. Try again.')
        continue
    
    splitted_user_name_string = user_name.split()

    if(splitted_user_name_string.__len__() != 2):
        print("Your name and surname, there should be only 2 words.")
        continue
    print(f"{splitted_user_name_string[0][0]}. {splitted_user_name_string[1][0]}.")
    break