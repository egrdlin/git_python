# Write a program to read through a mail log, build a histogram using a dictionary
# to count how many messages have come from each email address, and print the dictionary.

print('\033c') # clear the screen

while True:
    try:
        filename = input("Enter the file name: ")
        if len(filename) < 1:
            # press enter, it will open "mbox-short.txt" file by default
            filename = "mbox-short.txt"
        fhand = open(filename)
    except Exception as e:
        print("File can not be opened. Try again!")
        continue
    break
counts = dict()

for line in fhand: # read through each line
    if line.startswith("From "): # if the line starts with 'from'
        line = line.split() # split string line into list, its third address is the desired infomation
        print(line[1])
        # if this day is existed in dictionary, its count will be set to 1 as default, 
        # else, its current count increment by 1
        counts[line[1]] = counts.get(line[1],0) + 1 
            
print(counts)
print("\n\nThe most frequent email account is:\t", max(counts, key=counts.get), 
    "\tWith the count of: ", counts[max(counts, key = counts.get)],"\n\n") # print the maximum 
