#List Comprehension
    # Easier to write
    # used when you need to create a new list from an existent list
    # [expression for item in items]

fruits1 = ['avocado', 'banana', 'strawberry','kiwi', 'pineapple']
fruits2 = []

# for item in fruits1:
#     if 'n' in item:
#         fruits2.append(item)

# print(fruits2)

fruits2 = [item for item in fruits1 if 'n' in item]

print(fruits2)