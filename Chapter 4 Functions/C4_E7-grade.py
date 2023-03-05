try:
    inpScore = float(input("Enter score:\n"))
except:
        print("Bad score")
        input()

def computegrade(inpScore):

    try:
    
        if inpScore >= 0.9 and 1 > inpScore > 0:
            return("A")

        elif inpScore >= 0.8 and 1 > inpScore > 0:
            return("B")

        elif inpScore >= 0.7 and 1 > inpScore > 0:
           return("C")

        elif inpScore >= 0.6 and 1 > inpScore > 0:
            return("D")

        elif inpScore <0.6 and inpScore >0:
            return("F")

    except:
        return("Bad score")
        input()

print(computegrade(inpScore))
input()
