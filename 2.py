# 2. Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
#  для всех значений предикат.


import random

x = random.randint(0, 1)
y = random.randint(0, 1)
z= random.randint(0, 1)
print(f'x= {x}, y= {y}, z= {z}')

left_part = not(x or y or z)
right_part = not x and not y and not z
print (f'first_part = {left_part}    second_part = {right_part}')

if left_part == right_part:
    print('утверждение истинно')
else:
    print("утверждение ложно")