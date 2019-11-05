# Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with "From", then look for the third word and keep a running 
# count of each of the days of the week. At the end of the program print out the contents of your
#  dictionary (order does not matter).

while True:
    try:
        filename = input("Enter the file name: ")
        fhand = open(filename)
    except Exception as e:
        print("File can not be opened. Try again!")
        continue
    break
counts = dict()

for line in fhand: # read through each line
    if line.startswith("From "): # if the line starts with 'from'
        line = line.split() # split string line into list, its third address is the desired infomation
        # print(line[2])
        # if this day is existed in dictionary, its count will be set to 1 as default, 
        # else, its current count increment by 1
        counts[line[2]] = counts.get(line[2],0) + 1 
            
print(counts)
