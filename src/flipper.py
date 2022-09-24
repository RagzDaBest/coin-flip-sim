import random

heads = 0
tails = 0
flipped = 0
a = 0

print('Coin Flipping Simulator')
print('Enter the number of times you would like to flip a coin.')
flips = float(input())
print('')

while a < flips:
    flip = random.randrange(2)
    flipped = flipped + 1
    a = a + 1
    if flip == 0:
        heads = heads + 1
    else:
        tails = tails + 1
    print(flip, end=" ")

print(' ')
print('Results:')
print(f'Coins Flipped: {flipped}')
print(f'Percentage of Heads: {100/flips*heads}%')
print(f'Percentage of Tails: {100/flips*tails}%')
