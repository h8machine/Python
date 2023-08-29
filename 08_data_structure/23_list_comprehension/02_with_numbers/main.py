#List Comprehension
    # Easier to write
    # used when you need to create a new list from an existent list
    # [expression for item in items]

# values = []

# for x in range(6):
#     values.append(x * 10)

# print(values)

values = [x * 10 for x in range(6)] #does the same as lines 6 to 9
print(values)