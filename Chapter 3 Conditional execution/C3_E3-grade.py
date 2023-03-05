try:
    # input
    inpScore = float(input("Enter score:\n"))

    # output
    if inpScore > 1 or inpScore < 0:
        print("Bad score")
    elif inpScore >= 0.9:
        print("A")
    elif inpScore >= 0.8:
        print("B")
    elif inpScore >= 0.7:
        print("C")
    elif inpScore >= 0.6:
        print("D")
    else:
        print("F")
    input()

except:
    print("Bad score")
    input()
