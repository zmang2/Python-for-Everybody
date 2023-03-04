count = 0
number = 0

while True:
        line = input("Enter a number:")
        if line == "done":
            break
        
        try:
            count = count + 1
            inpNumb = line
            iterinpNumb = int(line)
            number = number + iterinpNumb
            average = number/count

        except:
            print("Invalid input")
            count = count - 1 

print("done")   
print(count)
print(number)
print(average)