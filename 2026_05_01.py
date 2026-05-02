# numbers = [10,20,30,40,50]

# string = "Hello"
# iterator = iter(string)
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))

# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break

####################################

# def generate_and_return_numbers():
#     numbers = []
#     for number in range(10):
#         numbers.append(number)
#     return numbers

# # list comperhetion
# def generate_and_return_numbers2():
#     return [number for number in range(10) if number % 2 == 0]

# print (generate_and_return_numbers2())

####################################

# from typing import Generator

# def range(start: int, stop: int, step: int) -> Generator[int, None, None]:
#     while start < stop - 1:
#         yield start 
#         # yield returns data like return without stopping the cycle
#         start += step

####################################

# def grep_errors_from_log(file_path: str):
#     with open(file_path, "r", encoding="utf-8") as file:
#         for line in file:
#             if "ERROR" in line:
#                 yield line.strip()

# user_input = input("Type log path: ")
# for i in grep_errors_from_log(user_input):
#     print(i)

####################################

# ПРАКТИЧНЕ ЗАВДАННЯ
# Потрібно реалізувати генератор adventure(), який моделює нескінченну послідовність подій у грі.
# Події не зберігаються наперед, а генеруються по одній під час ітерації.
# Кожен виклик next() повертає словник із описом події.

# Генератор має бути нескінченним (while True).
# Кожна подія – це словник з ключем “type”.
# Можливі типи подій: [“enemy”, “treasure”, “nothing”].
# Генерація типу подій: використовувати random.choice().
# Наповнення подій:
# - “damage”: випадкове число від 5 до 15.
# - “enemy_type”: один із “goblin”, “orc”, “skeleton”.
# - “treasure”: “gold”: випадкове число від 10 до 50
# - “nothing”: нічого, тільки “type”.

from typing import Generator
import random

def adventure() -> Generator[int, None, None]:
    action_type =   ["enemy",   "treasure", "nothing"   ]
    creature_type = ["goblin",  "skeleton", "ork"       ]
    while True:
        action = random.choice(action_type)
        match action:
            case "enemy":
                event_info = {
                    "type" : action,
                    "enemy_type": random.choice(creature_type),
                    "damage": random.randint(5,15)
                }
            case "treasure":
                event_info = {
                    "type" : action,
                    "gold": random.randint(10,50)
                }
            case "nothing":
                event_info = {
                    "type": action
                }
        yield event_info

actions = adventure()
prev = None
while 1:
    input("Press Enter to get an action!")
    temp = next(actions)
    while 1:
        if temp['type'] == prev:
            temp = next(actions)
        else:
            break
    prev = temp['type']
    print(temp)