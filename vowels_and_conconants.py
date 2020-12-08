def vowels (list, var):
    vow = []
    for i in var:
        if i in list:
            vow.append(i)
    return vow

def consonant (list, var):
    vow = []
    for i in var:
        if i not in list:
            vow.append(i)
    return vow


var = "perscholas"
list = ["a", "e", "i", "o", "u"]

print(vowels(list, var))
print(consonant(list, var))