# This program records the domain name (instead of the address) where the message was
# sent from instead of who the mail came from (i.e., the whole email address). At 
# the end of the program, print out the contents of your dictionary.



print('\033c') # clear the screen

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
        email = str(line[1]) # second address of the list is the desired field - email address
        index = email.find("@") # find the index
        email = (email[index+1:]) 
        print(email)
        # if this day is existed in dictionary, its count will be set to 1 as default, 
        # else, its current count increment by 1
        counts[email] = counts.get(email,0) + 1 
            
print(counts)
print("\n\nThe most frequent email account is:\t", max(counts, key=counts.get), 
    "\tWith the count of: ", counts[max(counts, key = counts.get)],"\n\n") # print the maximum 
