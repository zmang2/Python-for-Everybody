# input
    
inpHours = float(input("Enter hours\n"))
inpRate = float(input("Enter hourly rate\n"))
  
# output
if inpHours > 40:
    overtimeHours = inpHours - 40
    inpHours = 40
    pay = str((inpHours * inpRate)+(overtimeHours * (1.5*inpRate)))
    print("Pay: " + pay)
    input()
    
    
else: 
    inpHours <= 40
    pay = str((inpHours * inpRate))
    print("Pay: " + pay)
    input()
