# Lambda Function
    # it's a small function without name
    # can have lots of arguments, but only 1 expression
    # quite used in other functions
    # code becomes clean

def sum(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(sum(2))