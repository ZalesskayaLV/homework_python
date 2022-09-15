# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.

# Пример: -k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

n = int(input("Введите степень многочлена: "))

с_1 = [random.randint(10,100) for i in range (0, n+1)]
c_2 = ['x' if i < n else ' ' for i in range (0, n+1)]
c_3 = [i if i>1 else ' 'for i in range(n, -1, -1)]
new_lst = list(zip(с_1, c_2, c_3))
print(new_lst)

list_fnal = []
for i, item in enumerate (new_lst):
    new_lst[i]=list(filter(lambda a: a!="", new_lst[i]))
    new_lst[i]= "*".join(list(map(str, item)))

list_fnal = "+".join(new_lst)
print(list_fnal)

