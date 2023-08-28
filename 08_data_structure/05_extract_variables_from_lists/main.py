#unpacking lists
    # stores more than one information inside variables
    # they keep the data sequence inside a variable.
    # square brackets = []

products = ['arroz', 'feijão', 'maçã', 'banana', 1,2,3,4]

#using * to store all products starting from index 3 to index 6
item1, item2, item3, *others, item8 = products

print (item1)
print (item2)
print (others)
print (item8)