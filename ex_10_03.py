# Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the 
# letters a-z. Find text samples from several different languages and see how letter frequency 
# varies between languages
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # Configure the appearance of the plot

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
                    

print('\033c')
filename = input("Please enter the file name: ")
if len(filename) < 1: filename = "romeo.txt"

while True:
    try: 
        fhand = open(filename)
        print("Opening the file: ", filename, " \n\n...\n\n")
        time.sleep(0.5)
    except Exception as e:
        print("File cannot be opened. Try again!")
        continue
    break

file_contents = fhand.read() # read the whole file
file_contents = file_contents.lower() # convert every letter to letter

file_contents = file_contents.replace("\n","").replace(" ","") # remove new line characters and all white spaces
# print("\n",temp) # test 

letter_list= list(file_contents) # convert string contents into list
counts = dict() # creat a dictionary to counts the frequency of each letter

# print("Letter list: ",letter_list)
from string import ascii_lowercase

for letter in letter_list:
    counts[letter] = counts.get(letter,0) + 1

for letter in ascii_lowercase: # assign value 0 for each letter that is not existed in the file
    if letter not in counts:
        counts[letter] = counts.get(letter,0)

# print("dictionary counts: ", counts)
counts_list = sorted(counts.items()) # items() converts the dictionary to list, which allows sorted()
print("Sorted of counts: ", counts_list)

# print("Result:\n")
# for key,val in counts_list:
#     print(key,val)

sorted_count = [tup[1] for tup in counts_list] 
sorted_letter = [tup[0] for tup in counts_list] 

# print(sorted_count)

sum_counts = sum(sorted_count)
sorted_percentage = [(100 * x)  / sum_counts for x in sorted_count]
sorted_percentage = [round(x,2) for x in sorted_percentage]

# construct final result structure
result = list()
for i in range(0,len(sorted_count)):
    temp = (sorted_letter[i] , sorted_count[i], sorted_percentage[i])
    result.append(temp)

# rects_value = plt.bar(range(len(counts)), sorted_count, align='center') # label with count values
rects_percentage = plt.bar(range(len(counts)), sorted_percentage, align='center') # label with percentage

plt.xticks(range(len(counts)), sorted_letter)
plt.xlabel("Letter")
plt.ylabel("Counts")
plt.title("Letter frequency in the file")

print("letter|counts|percentage")
for val, key, per in result:
    print(val,"\t" ,key,"\t", per,"%")
autolabel(rects_percentage)
plt.show()

