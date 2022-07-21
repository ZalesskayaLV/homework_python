
import random

# составит список простых множителей числа N
def find_multipliers(num: int) -> list:
    mult_list = []
    for i in range(2, num):
        if num % i == 0 and exam(i):
            mult_list.append(i)
    return mult_list

# проверяет простой ли делитель
def exam(div):
    for i in range(2, int(div**0.5)+1):
        if div % i == 0:
            return False
    return True


# проверка на натуральное число
def input_number(text):
    while True:
        message = input(text)
        try:
            number = int(message)
            if number<=0:
                print("enter a natural number")
            else:
                return number
        except:
            print("error, you didn't enter a number!")


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



