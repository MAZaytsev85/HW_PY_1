import numpy as np

coin_quantity = input("Веедите колличесвто монет ")


arr = np.random.randint(0, 2, int(coin_quantity))
print(arr)

coin_count = 0
for i in arr:
    if i == 0:
        coin_count += 1
print(f"{coin_count} -> столько монет необходимо перевернуть")
