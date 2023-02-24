# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random

n = int(input('Введите длину первого множества -> '))
m = int(input('Введите длину второго множества -> '))

list_one = []
list_two = []
list_finish = []

for i in range(n):
    list_one.append(random.randint(1, 20))

for i in range(m):
    list_two.append(random.randint(1, 20))

print(list_one)
print(list_two)

for i in list_one:
    for j in list_two:
        if j == i:
            list_finish.append(j)

list_finish = list(set(list_finish))
print(list_finish.sort())
print(list_finish)
