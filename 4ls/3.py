# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

import random

# создает список из семи рандомных чисел от 1 до 9
def random_list_number():
    num_lst = []
    for i in range(7):
        r = random.randint(1, 9)
        num_lst.append(r)
    return num_lst

# выведет список неповторяющихся элементов исходной последовательности


def unic_list(lst: list):
    new_lst = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j] and i != j:
                break
        else:
            new_lst.append(lst[i])
    return new_lst


number_list = random_list_number()
print(number_list)
unic_number_list = unic_list(number_list)
print(unic_number_list)

