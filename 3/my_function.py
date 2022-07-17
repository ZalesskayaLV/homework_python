
import random

# создает список из семи рандомных чисел от 1 до 9
def random_list_number():  
    num_lst = []
    for i in range(7):
        r = random.randint(1, 9)
        num_lst.append(r)
    return num_lst


# находит сумму элементов списка, стоящих на нечетных позициях
def summ_el_odd_idx(lst_num: list):
    idx = 0
    summ = 0
    for item in lst_num:
        if idx % 2 != 0:
            summ += item
        idx += 1
    return summ


# находит произведение пар чисел из списка,
# парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.
def mult_pairs(lst_num: list):
    product = 1
    new_list = []
    length = len(lst_num)

    for i in range(0, length//2):
        product = lst_num[i]*lst_num[length - i - 1]
        new_list.append(product)
    if length % 2 != 0:
        new_list.append(lst_num[length//2]**2) # если список нечетной длины, то добавляется число без пары в квадрате
    return new_list



