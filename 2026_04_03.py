# student_info = {
#     'full_name': 'Andrew Yanush',
#     'age': 20,
#     'is_working': True,
# }

# print(student_info['full_name'])
# print(student_info.get('full_name'))
# print(student_info.get('fadasdull_name'))
# print(student_info.get('fadasdull_name', 'Bob'))

#####################################################

# product_info = {
#     'company': 'Apple',
#     'product': 'something',
#     'release_date': 2026,
#     'price': 1099.90
# }

# print(product_info.get('discount', 'nema nihuya'))

# product_info['discount'] = False
# print(product_info.get('discount', 'nema nihuya'))
# product_info.update({
#     'price':123123
# })
# print(product_info)

#####################################################

# first_student_info = {
#     'full_name': 'Andrew Yanush',
#     'age': 20,
#     'is_working': True,
#     'position': True
# }

# second_stdent_info = {
#     'full_name': 'Andrew Yanush',
#     'age': 20,
#     'is_working': True,
# }

# second_stdent_info.pop('pos', None)

# user_825947 = {
#     'full_name': 'Andrew Yanush',
#     'age': 20,
#     'is_working': True,
#     'email': 'something'
# }

# students_info = {
#     'name': 'CyberSec',
#     'course': 3,
#     'studets': [first_student_info, second_stdent_info],
# }

#####################################################

# numbers = [1,2,3,12,23,13,21,31,32,33,11,22]

# # for i in numbers:
# #     print(i)

# # for i in range(1,10,2):
# #     print(i)

# numbers.sort()
# t_num = 33

# # % - остача
# # // - націло

# #################
# # Binary search #
# #################
# def binary_search(arr, target_number):
#     l_indx, r_indx = 0, len(numbers) - 1
#     while l_indx <= r_indx:
#         m_indx = (l_indx + r_indx) // 2
#         print(arr[m_indx])
#         if(arr[m_indx] < target_number):
#             l_indx = m_indx+1
#         elif(arr[m_indx] > target_number):
#             r_indx = m_indx-1
#         else:
#             return m_indx
#     return False

# print("id:", binary_search())

#####################################################

# numbers = []

# # key-word continue - skips a one loop/circle
# while True: 
#     try:
#         user_number = int(input('Enter any number (-1 to exit): '))
#         if user_number == -1:
#             print('ok bye')
#             break
#         numbers.append(user_number)
#     except ValueError:
#         print('dude what the fuck is going on? only integer')

#####################################################

# import random
# import os

# bob = random.randint(1,4294967295)

# os.system('clear')
# print('From 1 to 4294967295, only natural numbers')
# while 1:
#     try:
#         guess = int(input('\nGuess number: '))
#         if guess != bob:
#             print('Hohoho - WRONG!')
#         else:
#             print('Dude, you fucking legend')
#         if guess < bob:
#             print('You number is lower than mine')
#             continue
#         print('Your number is higher than mine')
#     except ValueError:
#         print('You fucking retarded issue - only natural numbers')

#####################################################

# i=0
for i in range(2,1000,2):
    print(i)