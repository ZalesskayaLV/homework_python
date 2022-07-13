# 1. Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


def input_number(text):  # функция проверяет, что ввели вещественное число
    while True:
        message = input(text)
        try:
            number = float(message)
            return number

        except:
            print("error, you didn't enter a number!")


def summ_digit(num):
    if num < 0:
        num = num * -1
    summ = 0
    while num != 0:
        
        if num > 0:
            if num % 1 == 0:
                summ += num % 10
                num = num // 10
            else:
                num = num * 10
    return int(summ)





number = input_number('Введите число: ')
summ_digit_of_number = summ_digit(number)
print(summ_digit_of_number)



