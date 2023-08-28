'''
creating a 6x6 rectangle using nested loop

'''

lines = 6
columns = 6
symbol = '@'

for l in range(lines):
    for c in range(columns):
        print(symbol, end='')
    print()