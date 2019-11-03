# Write a program to read through the mail box data and when you find line that starts with "From", 
# you will split the line into words using the split function. We are interested in who sent the message, 
# which is the second word on the From line.

# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# You will parse the From line and print out the second word for each From line, 
# then you will also count the number of From (not From:) lines and print out a count at the end.

# prompt user to enter a approprite file name
while True:
    try:
        filename = input("Enter the file name: ")
        fhand =  open(filename)
    except Exception as e:
        print("File ' ",filename, "' couldn't be found. Retry again")
    break

count = 0
address_list = list() # declare a list where all email adresses will be stored

for line in fhand:
    if line.startswith("From:"): # if the line starts with 'From:'
        count +=1
        line = line.split() # split string into list
        print(line[1])
        address_list.append(line[1])
print("The number of Froms: ",count)



    