#lists
    # stores more than one information inside variables
    # they keep the data sequence inside a variable.
    # square brackets = []

customer_color= input('Type desired color.')
colors=['yellow','red','black','blue']

#using lower method to transform the input to lowercase
if customer_color.lower in colors:
    print('In stock')
else:
    print("We don't have this color in stock")