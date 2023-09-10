'''Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.'''

from random import randint
first_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(first_set)
second_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(second_set)
final_set = sorted(first_set.intersection(second_set))
print(*final_set)