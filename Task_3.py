


N = 10
K = 0
result = ""
while 2**K < N:
    result = result + str(2**K) + " "
    K += 1
print(result)