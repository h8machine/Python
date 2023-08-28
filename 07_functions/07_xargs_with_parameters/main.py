#functions
    #DRY = don't repeat yourself
    #xargs = several arguments * identifying the parameter **

# in this example, we have a function that stores numbers and strings (data).

def agency(**car): # the ** represent multi parameters
    return car


print(agency(brand='Gol',color='Branco',model=1.0))
print(agency(brand='Mitsubishi',color='Preto'))
print(agency(brand='Nissan'))