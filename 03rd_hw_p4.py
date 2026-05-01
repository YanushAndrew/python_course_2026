bob_interests = set()
not_bob_interests = set()

def user_input(res_set:set):
    input_value = input("Enter your interests, please!(divided by ',')")
    temp_set = set()
    temp_set = input_value.split(',')

    # word cleaning
    for i in range(0, temp_set.__len__(), 1):
        cur_word = str()
        for ch in temp_set[i]:
            if ch != ' ':
                cur_word += ch
        temp_set[i] = cur_word

    i=0
    while i < len(temp_set):
        if temp_set[i].__len__() > 0:
            i += 1
        else:
            temp_set.pop(i)
    res_set.update(temp_set)
    return

def print_set(some_set:set):
    temp_string = str()
    try: 
        if(some_set.__len__() < 1):
            print("Your current list of interests - empty.")
            return
        for word in some_set:
            temp_string += word
            temp_string += ', '
        print("Your current list of interests: ", temp_string[0:-2])
    except ValueError:
        print("I guess, that is not set-object.")

while 1:
    user_identity = input('Are you Bob?(1 - yes, 2 - no): ')
    try:
        match int(user_identity):
            case 1:
                print("Happy to see you!")
                print_set   (bob_interests)
                user_input  (bob_interests)
            case 2:
                print("Okay")
                print_set   (not_bob_interests)
                user_input  (not_bob_interests)
            case _:
                print("stupid")
    except ValueError:
        print("You are more than retarded...")