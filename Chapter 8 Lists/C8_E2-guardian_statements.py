# Exercise 2:
# Figure out which line of the above program is still not
# properly guarded. See if you can construct a text file which causes the
# program to fail and then modify the program so that the line is properly
# guarded and test it to make sure it handles your new text file.

## A lime with "From" as the 1th element but, only 2 elements long would break the program
##i.e a list with a 1th and 2th element, but not a 3th element in this case would be the "day"
##this would produce an IndexError.


#fhand = open('mbox-short.txt')
#hand = ["From Greg"]

fhand = open("zbreak.txt") #break.txt is a created text file which breaks the program
count = 0

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0: continue
    if len(words) < 3: continue #this extra guardian statement only prints the line if there is a 3th element after "From" and "Name"
    if words[0] != 'From' : continue
    print(words[2])