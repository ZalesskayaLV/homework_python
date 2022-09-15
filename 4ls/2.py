# 2.Задайте натуральное число N. 
# Напишите программу, которая составит
#  список простых множителей числа N.

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


number = int(input("введите число: "))
lst = find_multipliers(number)
print(lst)
