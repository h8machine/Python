# Set (lists)
    # Similar to lists
    # They avoid duplicated items
    # They don't use indexing

set1 = {'a','b','c'}
set2 = {'a','d','e'}

set3 = set1.union(set2)
set4 = set1.difference(set2)
set5 = set1.intersection(set2)
set6 = set1.symmetric_difference(set2)

print(set3)
print(set4)
print(set5)
print(set6)