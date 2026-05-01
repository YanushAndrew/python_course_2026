custom_set = [1,2,3,4,5]
while 1: 
    user_value = input("You can add something(number) to the set: ")
    try:
        if(custom_set.count(int(user_value)) >= 1):
            print("This value is already exists in the set. Set remains unchanged.")
        else:
            print(custom_set)
            custom_set.append(int(user_value))
            print(custom_set)
    except ValueError:
        print("Please, enter interger number.")
        continue