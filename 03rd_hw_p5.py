number_str = input("Input some numbers(separated by spaces): ")
number_set = number_str.split(' ')
print (number_set)
all_ok = True
for o in number_set: 
    try:
        temp = int(o)
    except ValueError:
        print("Not all element - integer number.")
        all_ok = False
        break

sum = int()
if(all_ok):
    for i in number_set:
        sum += int(i)
    print (sum)
