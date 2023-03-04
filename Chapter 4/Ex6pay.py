try:
    # input
    
    inpHours = float(input("Enter hours\n"))
    inpRate = float(input("Enter hourly rate\n"))

    # output
    def computepay(inpHours,inpRate):
        if inpHours > 40:
            overtimeHours = inpHours - 40
            inpHours = 40
            payment = str((inpHours * inpRate)+(overtimeHours * (1.5*inpRate)))
            
        else: 
            inpHours <= 40
            payment = str((inpHours * inpRate))

        return payment

    pay = computepay(inpHours,inpRate)
    print("Pay: ",pay)
    input()

except:
    print("Error, please enter a numeric input")
    input()
