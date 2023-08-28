#lists
    # stores more than one information inside variables
    # they keep the data sequence inside a variable.
    # square brackets = []

# create a fruit list from an input provided by an user.

user_fruits = input('Type the name of fruits separated by comma (,):')

#transforming inputs in a list considering comma as separator
fruits_list = user_fruits.split(', ')

print(fruits_list)