#DRY = don't repeat yourself
#parameter --> argument

def welcome_user(name, amount):
    print(f'Olá {name}. Seja bem vindo')
    print(f'Temos {str(amount)} laptops em estoque')

welcome_user('Diogo', 10)
welcome_user('Mia', 15)
welcome_user('Abella', 8)