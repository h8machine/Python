# Set (lists)
    # Similar to lists
    # They avoid duplicated items
    # They don't use indexing

list1 = [10,20,30,40,50]
s1 = {1,2,3,4,5,6}

s1.add(7)
s1.update([6,7,8,9,10]) #adding more than 1 item into set

s1.discard(11) 
# s1.remove(11)

print(s1)