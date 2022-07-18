# 3 - Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.567, 10.03] => 0.564 или 564

from my_function import fractional_diff


float_num_list = [1.1, 1.2, 3.1, 5.567, 10.003]
print(float_num_list)

difference = fractional_diff(float_num_list)
print(difference)
