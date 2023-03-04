#Exercise 3: Encapsulate this code in a function named count, and gen-
#eralize it so that it accepts the string and the letter as arguments.

#word = 'banana'
#count = 0
#for letter in word:
#        if letter == 'a':
#           count = count + 1
#print(count)

cword = input("What world would you like to choose?")
cletter = input("What letter in the word would you like to count?")

def count(word,letter):
    lcount = 0
    for letter in word:
        if letter == cletter:
            lcount = lcount + 1
    return lcount

x = count(cword,cletter)
print(x)