# Write another program that prompts for a list of numbers as above and at the end prints out both the
#  maximum and minimum of the numbers

maximum = None
minimum = None

while(True):
    val = input("Enter a number: ")
    if val == "done": 
        print("All done")
        break
    try:
        fval = float(val)

    except Exception as e:
            print("invalid input")
            continue
    
    if maximum is None or (fval > maximum):
        maximum = fval
    if minimum is None or (fval < minimum):
        minimum = fval

print("Maximum value entered: ", maximum, "\tMinimum value entered: ", minimum)

