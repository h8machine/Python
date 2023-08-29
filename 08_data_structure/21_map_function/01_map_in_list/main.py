#Map Function
    # quite used in lists
    # apply a function in a Iterable, in each item. (list, tuple, dictionary etc)

list1 = [1,2,3,4]

def multi(x):
    return x * 2

list2 = map(multi, list1) # list items * 2 of function multi

print(list(list2))