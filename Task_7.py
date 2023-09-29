'''Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''

from random import randint

list_1 = [randint(-10, 10) for i in range(20)]
print(list_1)
list_2 = []

min_value = int(input('Введите минимальное значение '))
max_value = int(input('Введите максимальное значение '))

for i in list_1:
    if min_value <= list_1[i] <= max_value:
        list_2.append(list_1[i])

print(list_2)
