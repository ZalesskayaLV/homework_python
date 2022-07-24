# 1 - Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi,
# а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.

# Пример:

# - при d = 0.001, π = 3.141.    10 ^ (-10)≤ d ≤10 ^ -1

from functions_4 import number_Pi
p = number_Pi()
print(p)

# 2 - Задайте последовательность чисел. Напишите программу, которая выведет
#  список неповторяющихся элементов исходной последовательности. 
# Посмотрели, что такое множество? Вот здесь его не используйте.

from functions_4 import random_list_number, unic_list

number_list = random_list_number()
print(number_list)
unic_number_list = unic_list(number_list)
print(unic_number_list)

# 3 - Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

from functions_4 import find_multipliers, input_number
number = input_number("введите число: ")
lst = find_multipliers(number)
print(lst)

# 4 - В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

# https: // zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
# Это на случай возникновения непонятных символов в файле.

file = open ('data.txt', 'r', encoding = 'utf-8')
data = file.read()
text = data.split()
print(text)
new_text = []

for word in text:
    if word.isalpha():
        new_text.append(word)
print(new_text)
file.close()


with open ('data.txt', 'w', encoding= 'utf-8') as text:
    for i in new_text:
        text.write(f'{i} ')
#     text. write(''.join(new_text))
text.close()



