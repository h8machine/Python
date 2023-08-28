'''
=== for loop: nested ===

A loop inside another.

-Outer loop
    -Inner loop
'''

for numero1 in range(1,6): #outer loop
    print(f'Produto {numero1}')
    for numero2 in range(5): #inner loop
        print(numero1, numero2)