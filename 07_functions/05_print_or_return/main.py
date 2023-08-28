#functions
    #they do tasks
    #DRY = don't repeat yourself
    #calculate and return a value

    #print function does not store values!
    #use RETURN if you want to use the variable later.

def customer1(name):
    print(f'Olá {name}')

def customer2(name):
    return f'Olá {name}'


x = customer1('Diogo')
y = customer2('Ana')

print(x)
print(y)