# 5 - Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи](https://clck.ru/sH87m)

from my_function import fibo, input_number

N = input_number("Введите число: ")
print(fibo(N))