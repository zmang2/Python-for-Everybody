# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.
t = [1,2,3,4,5]

def chop(t):
    del t[0]
    del t[len(t)-1]

t2 = chop(t)

print(t)
print(t2)