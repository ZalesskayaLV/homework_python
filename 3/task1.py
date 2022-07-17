# 1 - Задайте список из нескольких чисел.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример: *

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from my_function import random_list_number, summ_el_odd_idx

list_number = random_list_number()
print(list_number)

summ_elements = summ_el_odd_idx(list_number)
print(f'сумма элементов, стоящих на нечетных позициях: {summ_elements}')
