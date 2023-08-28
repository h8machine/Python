#lists
    # stores more than one information inside variables
    # they keep the data sequence inside a variable.
    # square brackets = []

cities = ['São Paulo', 'Rio de Janeiro', 'Santos'] 

cities[0] = 'Pinda'

cities.append('Taubaté') #append method adds an item at the end of list
cities.remove('Pinda')
cities.insert(1 , 'Campinas')
cities.pop(0) #pop method removes indicated index
cities.sort()

print(cities)
print(cities[2])