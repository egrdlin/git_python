# Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out\
# the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using
# try and except and print an error message and skip to the next number.
num = 0
tot =0.0
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
    num = 1+num
    tot = tot + fval
print("Numbers entered:", num, "\nSum: ", tot, "\nAaverage:", tot/num)

