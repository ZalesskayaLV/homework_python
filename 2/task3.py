# 3 - Задайте список из n чисел последовательности(1+1/n)**n
#  и выведите на экран их сумму.

# *Пример: *

# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}


def input_number(text):  # функция проверяет, что ввели число
    while True:
        message = input(text)
        try:
            number = int(message)
            if number <= 0:
                print('enter a number greater than zero')
            else:
                return number

        except:
            print("error, you didn't enter a number!")


Num = input_number('Введите число N: ')

numbers_list = {}
for i in range(1, Num+1):
    numbers_list[i] = (1+1/i)**i
    
print(numbers_list, sep=', ')
