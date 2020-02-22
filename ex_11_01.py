#  Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that
#  matched the regular expression
import re
while True:
    try:
        filename = input("Enter the file name:")
        if len(filename) <1 : filename = "mbox.txt"
        fhand = open(filename)
        print("Opening file '{}'...\n".format (filename))
    except Exception as e:
        print("Can't open the file")
        continue
    break
    

count = 0

expression = input("Please enter the regular expression:")

for line in fhand:
    line = line.rstrip()
    result = re.search(expression, line)
    if result:
        count += 1
print(filename + " had " + str(count) + " line that matched " + expression + "\n")