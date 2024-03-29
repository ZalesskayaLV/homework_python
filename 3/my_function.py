
import random

# создает список из семи рандомных чисел от 1 до 9
def random_list_number():
    num_lst = []
    for i in range(7):
        r = random.randint(1, 9)
        num_lst.append(r)
    return num_lst

# функция проверяет, что ввели число
def input_number(text):
    while True:
        message = input(text)
        try:
            number = int(message)
            return number

        except:
            return False


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
        # если список нечетной длины, то добавляется число без пары в квадрате
        new_list.append(lst_num[length//2]**2)
    return new_list

# находит разницу между максимальным и минимальным значением дробной части элементов
def fractional_diff(num_list: list):
    nums = []
    for item in num_list:
        t = round(item % 1, 3)
        nums.append(t)
        max_num = nums[0]
        min_num = nums[0]
        for i in range(0, len(nums)):
            if nums[i] < min_num:
                min_num = nums[i]
            else:
                max_num = nums[i]
        diff = round(max_num - min_num, 3)
    return diff

# переводит число из десятичной системы в двоичную
def from_decimal_to_binary(number: int):
    result: str = ""
    if number == 0:
        result = 0
    elif number < 0:
        number *= -1
    while number > 0:
        remainder = number % 2
        number = number // 2
        result = (str(remainder)) + result  
    return result


def fibo(number: int):
    fibo = [0, 1]
    if number == 0:
        fibo = [0]
    elif number == 1:
        fibo = [0, 1]
    elif number == -1:
        fibo = [1]
    elif number < 1:
        for i in range(number, -2):
            fibo.append(fibo[i+2] - fibo[i+1])
        # return fibo.reverse()
    else:
        for i in range(2,number+1):
            fibo.append(fibo[i-1]+fibo[i-2])
    return  fibo
