# This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the "From" line by finding the time string and then
# splitting that string into parts using the colon character. Once you have accumulated 
# the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
import time
print('\033c')

filename = input("Enter the file name: ")

while True:
    if len(filename) < 1 : filename = "mbox-short.txt"
    try:
        fhand = open(filename)
        print("Opening File:\t", filename)
        time.sleep(0.5)
    except Exception as e:
        print("File can not be opened, please try again!")
        continue
    break
hour = list()
hour_counts = dict()

for line in fhand:
    if line.startswith("From "):
        # print(line)
        line = line.split() # stirng to list
        # print(line[5]) 
        temp = line[5] # obtain the hour from the list
        hour.append(temp[:2]) # append hour detail into a list
        hour_counts[temp[:2]] = hour_counts.get(temp[:2],0) + 1 # using dictionary to count the frequency

# print("Stored list of hour info: ", hour)
# print("\nUnsorted dictionary hour counts: ", hour_counts)


hour_counts_list = sorted(hour_counts.items(), reverse=False) # Note: items() function converts dict to list

for key,val in hour_counts_list: # print the output
    print(key,val)

    
   