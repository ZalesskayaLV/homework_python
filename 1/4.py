# 4-Напишите программу, которая
#  по заданному номеру четверти,
#  показывает диапазон возможных координат
#  точек в этой четверти(x и y).


quater = int(input('enter quater number: '))

while quater in range(1, 5):
    if quater == 1:
        print(' x > 0, y > 0 ')
        break
    elif quater == 2:
        print(' x < 0, y > 0')
        break
    elif quater == 3:
        print(' x < 0, y < 0 ')
        break
    elif quater == 4:
        print(' x > 0, y < 0 ')
        break
else:
    print('just four quarters in Cartesian coordinate system')
