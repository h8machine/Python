'''
=== While Loop ===

Used for loops that depends of a condition.

In this example, we'll publish a product with 10% commission if it costs more than R$20
'''

value = int(input('Digite o valor do Produto (R$): '))

while value > 20:
    value = (value * 0.10) + value
    print(f'O valor final do seu produto será de R${value}')
    break