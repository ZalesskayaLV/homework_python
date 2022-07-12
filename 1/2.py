# 2. Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
#  для всех значений предикат.


for x in range (0, 2):
    for y in range (0, 2):
        for z in range (0, 2):
            left_part = not(x or y or z)
            right_part = not x and not y and not z
            print(f'{x, y, z}     {left_part}         {right_part}')

if left_part == right_part:
    print('утверждение истинно')
else:
    print("утверждение ложно")