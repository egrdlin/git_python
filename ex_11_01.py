#  Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that
#  matched the regular expression
import re

filename = input("Please enter the file name: ")
if len(filename) < 1: filename = "mbox.txt"

while True:
    try: 
        fhand = open(filename)
        print("Opening the file: ", filename, " \n\n...\n\n")
    except Exception as e:
        print("File cannot be opened. Try again!")
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