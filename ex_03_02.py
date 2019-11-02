try:
    hour = int(input("Enter Hours: "))
except:
    print("Error, please enter numeric values")
    quit()

try:
    rate = int(input("Enter Rate: "))
except:
    print("Error, please enter numeric values")
    quit()

if hour>40:
    overtime = hour-40
    payment = overtime * rate * 1.5 + 40 * rate
else:
    payment = hour * rate
print("Hours worked: ", hour,'\n Payment: ', payment)