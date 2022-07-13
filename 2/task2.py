# 2 - Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


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

numbers_list = []
result = 1
for i in range(1, Num+1):
    result *= i
    numbers_list.append(result)
print(numbers_list, sep=', ')