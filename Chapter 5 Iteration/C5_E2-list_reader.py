## initialisation

minimum = 0
maximum = 0
smallest = None
largest = None

while True:
    line = input("Enter a number:")
    if line == "done":
        break

    try:
        minimum = int(line)
        maximum  = int(line)

        if smallest is None or minimum < smallest:
            smallest = minimum

        if largest is None or maximum > largest:
            largest = maximum

        print("Loop smallest: ",minimum,smallest)
        print("Loop largest: ",maximum,largest)

    except:
        print("Invalid input")
    
print("Minimum: ",smallest)
print("Maximum: ",largest)