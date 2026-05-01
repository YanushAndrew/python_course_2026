# python_course_hw_2

EXCHANGE_RATE_USD_TO_UAH = 43.9205
EXCHANGE_RATE_EUR_TO_UAH = 50.8951

def is_float(data):
    try:
        i = float(data)
    except:
        return 0
    return 1

def exchange_print(amount):
    print(f"В євро: \t{amount*EXCHANGE_RATE_EUR_TO_UAH}") 
    print(f"В доларах: \t{amount*EXCHANGE_RATE_USD_TO_UAH}") 

while 1:
    userInputAmount = input("Скільки гривень ви бажаєте обміняти: ")
    if is_float(userInputAmount):
        exchange_print(float(userInputAmount))
    else:
        print("dude you should write something without letters, special symbols or \",\"")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n")