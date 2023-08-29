# Lambda Function
    # it's a small function without name
    # can have lots of arguments, but only 1 expression
    # quite used in other functions
    # code becomes clean

# def sum(x):
#     return x + 10

# print(sum(2))

sum10 = lambda x: x+10 #does the same as line 7 to 10
sum16 = lambda y,z: y+z+10 

print(sum10(2))
print(sum16(2,4))