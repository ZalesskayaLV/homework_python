# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример: *

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from my_function import input_number, from_decimal_to_binary


number = input_number('введите число: ')
result = from_decimal_to_binary(number)
print(result)



