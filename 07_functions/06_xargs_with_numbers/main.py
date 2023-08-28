#functions
    #DRY = don't repeat yourself
    #xargs = several arguments

# in this example, we have a function that sum several numbers.

def sum(*numbers): # the * represent multi arguments
    result = 0
    for num in numbers:
        result += num
    return result

x= sum(2,2,2,2,2)

print(x)