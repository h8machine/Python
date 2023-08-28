#lists
    # stores more than one information inside variables
    # they keep the data sequence inside a variable.
    # square brackets = []

numbers = [2,3,4,5]
letters = ['a','b','c','d']
items = [['item1','item2'],['item3','item4']] #list with sublists

#end = numbers + letters

numbers.extend(letters) #does the same as line  10

print(numbers)
print(items[0])