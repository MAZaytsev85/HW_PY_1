#Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.


N = int(input("Введите число N "))
K = 0
result = ""
while 2**K < N:
    result = result + str(2**K) + " "
    K += 1
print(result)

#for commit 1