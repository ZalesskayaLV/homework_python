# 2 - Напишите программу, которая найдёт произведение
#  пар чисел списка. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from my_function import random_list_number, mult_pairs

list_number = random_list_number()
print(list_number)

product_numbers = mult_pairs(list_number)
print(product_numbers)

