from random import randint

def lower_case(list, letter):
    return list.count(letter)

list = []; letter = chr(randint(97, 122))

for i in range(10):
    list.append(chr(randint(97, 122)))

print(list)
print(letter)
print(lower_case(list, letter))