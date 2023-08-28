from array import array

#Array (matrix)
    # Similar to lists
    # Better performance

letters = ['a', 'b', 'c', 'd']
numbers_i = [10, 20, 30, 40]
numbers_f = [1.2, 1.3, 1.4]

print(letters)
print(numbers_i)
print(numbers_f)
print()

letters = array('u', ['a', 'b', 'c', 'd']) # 'u' is for strings
numbers_f = array('i', [10, 20, 30, 40]) # 'i' is for integer
numbers_i = array('f', [1.2, 1.3, 1.4]) # 'f' is for float

print(letters)
print(numbers_f)
print(numbers_i)