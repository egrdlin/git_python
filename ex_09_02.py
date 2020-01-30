# Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with "From", then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print out the contents of your
#  dictionary (order does not matter).

print('\033c')  # clear the screen

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

for line in fhand:  # read through each line
    if line.startswith("From "):  # if the line starts with 'from'
        line = line.rstrip()
        # split string line into list, its third address is the desired infomation
        line = line.split()
        # print(line)

        # line[0] - "From"
        # line[1] - email address
        # line[2] - day
        # line[3] - month
        # line[4] - date
        # line[5] - time
        # line[6] - year

        # print(line[2])
        # if this day is existed in dictionary, its count will be set to 1 as default,
        # else, its current count increment by 1
        counts[line[2]] = counts.get(line[2], 0) + 1

print(counts)

# now find the most common day
largest = 0
theword = None

for key,val in counts.items():
    print(key,val)
    if val>largest: 
        largest = val
        theword = key

print("Found:", theword,largest)

