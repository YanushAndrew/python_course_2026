# try:
#     first_var = 10
#     second_num = 0
#     print (first_var/second_num)
# except:
#     print('some shit happened')

#############################################

# first_var = 10
# second_num = '0'
# # не вставляти в try інформацію, котра не може викликати помилку
# try:
#     print (first_var/second_num)
# except (ZeroDivisionError, TypeError) as error:
#     print(error)

#############################################

# user_input = input('enter a number: ')
# try:
#     number = int(user_input)
# except ValueError:
#     print('invalid imput, not int')
# else:
#     print(number ** 2)
# finally:
    # print('end of the try-block')

#############################################

# def risky_operation(): ...
# def log_error(error): ...
# def save_result(result): ...
# def cleanup(): ...

# try:
#     result = risky_operation()
# except Exception as error:
#     log_error(error)
# else:
#     save_result(result)
# finally:
#     cleanup()

#############################################

# Треба використовуючи блок `try...except` обробити помилки, які можуть виникнути при виконанні наступного коду.
# Оцінка має бути числом від 0 до 100.

def add_grade(grades: list[int]) -> None:
    grade = float(input("Введіть оцінку: "))
    grades.append(grade)


def calculate_average(grades: list[int]) -> float:
    try:
        res = sum(grades) / len(grades)
    except (ZeroDivisionError, TypeError) as err:
        return err
    else:
        return res


def show_by_index(grades: list[int]) -> None:
    try:
        index = int(input("Введіть індекс: "))
    except TypeError as err:
        print(err)
    else:
        print(f"Оцінка: {grades[index]}")


def main() -> None:
    user_grades = input("Введіть оцінки через пробіл: ")
    if not user_grades:
        print('...')
        return
    try:
        grades = [float(grade) for grade in user_grades.split()]
    except TypeError as error:
        print(error)
    else:
        add_grade(grades)

        average_grade = calculate_average(grades)
        print(f"Середня оцінка: {average_grade}")

        show_by_index(grades)


main()
