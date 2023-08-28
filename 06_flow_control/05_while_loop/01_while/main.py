'''
=== While Loop ===

Used for loops that depends of a condition.

In this example, we'll create a sale for a product that costs R$100
'''

value = 100
day = 1

while value > 20:
    day+= 1
    print(f'On day {day} the product will be sold for R${value}')
    value -= 5