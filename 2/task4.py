# 4. Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

import time

num_list = [1, 3, 7, 9, 2, 4]

num_rand = str(time.time_ns())

print(num_list)
print(num_rand)

for i in range(0, len(num_list)):
    for j in num_rand:
        if int(j) < len(num_list):
            num_list[i], num_list[int(j)] = num_list[int(j)], num_list[i]

print(num_list)
