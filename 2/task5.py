# Задайте список из N элементов, заполненных числами из промежутка[-N, N].
#  Найдите произведение элементов на указанных позициях.
#   Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

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

N = input_number('Введите число N: ')
my_list = []
for i in range (-N, N):
    my_list.append(randint(-N,N+1))
print(my_list)


with open ('file.txt', mode = 'r') as file:
    result = 1
    lst_index = []
    for line in file.read():
        if line.isdigit():
            result*= my_list[int(line)]
            lst_index.append(line)

print(f'{lst_index = }')
print(f'{my_list =}')
print (result)
