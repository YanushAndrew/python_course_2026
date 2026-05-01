# user_info = {
#     "name": "Something",
#     "age": 30,
#     "city": "anything",

# }

# def greet(user):
#     name = user.get("name", "User")
#     print(f"Good morning, {name}!")

# greet(user_info)

# ------------------------------------------------------------

# def count_price_with_discount(price, disount):
#     discounted_price = price * (1-disount)
#     return round(discounted_price)
#     # print(round(discounted_price))

# count_price_with_discount(123123,.2)

# ------------------------------------------------------------

# def adding(a,b):
#     return a+b

# def substract(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

# def divide(a,b):
#     if b == 0:
#         # return 0
#         raise ValueError("на нуль ділити не можна")
#     return a/b

# divide(1,0)

# ------------------------------------------------------------

# user_info = {
#     "name" : "something",
# }

# # можна вказати значення за замовчуванням ля параметру функції
# def greet(user, message = "Hello"):
#     print(message, user.get("name"))

# greet(user_info)

# def something(l:list | int, bob):
#     return "loh"

# ------------------------------------------------------------

import random
import os

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

def password_generator(length:int,ltr:bool, smbl:bool, nmbr:bool) -> str:
    symbol_set = str()
    res = str()
    if ltr :
        symbol_set+=LETTERS
    if smbl :
        symbol_set+=SYMBOLS
    if nmbr :
        symbol_set+=DIGITS
    for i in range(0, length, 1):
        o = random.randint(0, symbol_set.__len__()-1)
        res += symbol_set[o]
    return res

while 1: 
    print("Шо ти голова, сука, пароль зараз будемо створювати тобі, блядь!")
    try:
        pass_length = int(input("Так шо, яка довжина пароля буде?: "))
    except:
        print("ну ти намудрив, сука, нармально пиши")
        continue

    include_letters = (input("Літери y/n: ").lower() == 'y')
    include_numbers = (input("Числа y/n: ").lower() == 'y')
    include_symbols = (input("Особливі y/n: ").lower() == 'y')
    print(include_letters,include_numbers,include_symbols)

    if not (include_letters or include_numbers or include_symbols):
        print("Не соромся, блять, обери щось")
        continue
    data = password_generator(pass_length, include_letters, include_symbols, include_numbers)
    print(data)

    os.system(f'echo {data} | xclip -selection clipboard && echo "Copied to the clipboard!"')