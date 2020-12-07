from random import choice

def suit (x):
    if x // 13 == 0:
        return "Spades"
    elif x // 13 == 1:
        return "Hearts"
    elif x // 13 == 2:
        return "Diamonds"
    else:
        return "Clubs"

def number (x):
    list_numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    return list_numbers[x%13]

deck = []
for i in range(52):
    deck.append(i-1)

card = choice(deck)

print (card)
print(number(card) + " of " + suit(card))

