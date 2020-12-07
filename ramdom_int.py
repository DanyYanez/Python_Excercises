import random

list = []; average = 0; count = 0

for i in range(9):
    list.append(random.randint(0, 10))
    average += list[i]

average /= len(list)

for i in list:
    if i > average:
        count += 1

print(list)
print(int(average))
print(count)