#Map Function
    # quite used in lists
    # apply a function in a Iterable, in each item. (list, tuple, dictionary etc)

list1 = [1,2,3,4]

# def multi(x):
#     return x * 2

# list2 = map(lambda x: x * 2, list1)

print(list(map(lambda x: x * 2, list1)))