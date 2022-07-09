# Напишите программу, которая принимает на вход
#  координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
#  и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# def input_number(message):  (DO NOT WORK! NEED TO THINK MORE)
#     while True:
#         try:
#             number = int(message)
#             return number
                
        
#         except:
#             print("error, you didn't enter a number!")
#             break


def quarter_search(x, y):
    if x>0 and y>0:
        return 1
    elif x>0 and y<0:
        return 4
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3



x = int(input('enter coordinate x: '))
y = int(input('enter coordinate y: '))

if x==0 or y==0:
    print('enter coordinates different from zero')
else:
    result = quarter_search(x, y)
    print(f'coordinates are in {result} quarter')




    

