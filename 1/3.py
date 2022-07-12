# Напишите программу, которая принимает на вход
#  координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
#  и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# def input_number(message):
#     while True:
#         value_input = input(message)
#         char = 1
#         if value_input.startswith() == '-':
#           char = -1
#           if not value_input.isdigit():
#               print("error, you didn't enter a number!")
#           elif value_input == 0:
#               print('null is not correct')
#           else:
#               return value_input*char

def input_number(text):
    while True:
        message = input(text)
        try:
            number = int(message)
            if number == 0: 
                print('null is not correct')
            else:
                return number

        except:
            print("error, you didn't enter a number!")



def quarter_search(x, y):
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3


x = input_number('enter coordinate x: ')
y = input_number('enter coordinate y: ')


result = quarter_search(x, y)
print(f'coordinates are in {result} quarter')
