def odd (x, y):
    list = []
    while len(list) < y:
        if x % 2 != 0:
            list.append(x)
        x += 1
    return list

x = int(input("Start number: "))
y = int(input("Number of odds: "))

print(odd(x, y))