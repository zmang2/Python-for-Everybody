# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

t = [1,2,3,4,5]

def middle(t):
    return t[1:len(t)-1]

t2 = middle(t)
print(t,t2)