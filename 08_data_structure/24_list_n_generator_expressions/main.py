from sys import getsizeof

# Generator Expressions
    # a faster way for lists, dictionaries etc.
    # less memory allocation
    # bytes values

numbers = [x * 10 for x in range(500)] #list
print(type(numbers))
# print(numbers)
print(getsizeof(numbers))

print('------')

numbers = (x * 10 for x in range(500)) #generator expression
print(type(numbers))
# print(list(numbers))
print(getsizeof(numbers))