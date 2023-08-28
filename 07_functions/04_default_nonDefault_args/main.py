#DRY = don't repeat yourself
#parameter --> argument
#default = the one that you define the parameter value
#non-default = the one that you DON'T define the parameter value

#NON DEFAULT PARAMETER COMES FIRST, ALWAYS!

def welcome_user(amount, name='Diogo'):
    print(f'Olá {name}. Seja bem vindo')
    print(f'Temos {str(amount)} laptops em estoque')

welcome_user(10)