# Read from a file.
#  print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
#  sort the list in reverse order and print out the person who has the most commits.
print("\033c")
while True:
    filename = input("Enter the file name: ")
    if len(filename) < 1: filename = "mbox-short.txt"
    try:
        fhand = open(filename)
    except Exception as e:
        print("The file can not be opened. Try again!")
        continue
    break
email_counts = dict()
for line in fhand:
    if line.startswith("From "):
        line = line.split()
        email = line[1]
        email_counts[email] = email_counts.get(email,0) + 1 # create a dictionary of email address and its count
# print(email_counts)

# create a list of tuples that has value key pair to allow sort or other functions based on the value element
email_list = list()
for key,value in email_counts.items():
    email_tuple = (value,key)
    email_list.append(email_tuple) # append tuples to the list
# print(email_list) 

email_list = sorted(email_list, reverse=True) # sort by value (frequency)

# print(email_list) # print the sorted email list of tuples

# construct a new list with key-value tuples instead of value-key pair. 
# Tuples are immutable, thus, we need construct a new variable for the rearrangement
sorted_email_list = list()
for key,value in email_list:
    tur = [value,key]
    sorted_email_list.append(tur)
print("Most frequent users: ",sorted_email_list[0])

