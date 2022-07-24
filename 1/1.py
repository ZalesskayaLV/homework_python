# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def input_number(text):
    while True:
        message = input(text)
        try:
            number = int(message)
            return number
        except:
            print("error, you didn't enter a number!")
            



day_of_week = input_number('Введите цифру от 1 до 7, обозначающую день недели: ')

if day_of_week in range(1, 6):
    print("нет")
elif day_of_week in range(6, 8):
        print('да')
else: 
    print("введите число от 1 до 7")

