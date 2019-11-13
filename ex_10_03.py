# Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the 
# letters a-z. Find text samples from several different languages and see how letter frequency 
# varies between languages
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

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
# print("Sorted of counts: ", counts_list)

print("Result:\n")
for key,val in counts_list:
    print(key,val)


plt.bar(range(len(counts)), list(counts.values()), align='center')
plt.xticks(range(len(counts)), list(counts.keys()))
plt.xlabel("Letter")
plt.ylabel("Counts")
plt.title("Letter frequency in the file")
/**
#FIXME:Add values and percentile to the bar plot
# def autolabel(rects):
#     # attach some text labels
#     for rect in rects:
#         height = rect.get_height()
#         plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,
#                 '%d' % int(height),
#                 ha='center', va='bottom')
# rects1 = plt.bar(np.arange(len(labels)) - width/2, men_means, width, label='Men')
# autolabel(rects1)


plt.show()



# # example program to test if the matplotlib is installed properly in the local environment
# x = np.arange(0.1, 4, 0.1)
# y = np.exp(-x)

# # example variable error bar values
# yerr = 0.1 + 0.1 * np.sqrt(x)


# # Now switch to a more OO interface to exercise more features.
# fig, axs = plt.subplots(nrows=1, ncols=2, sharex=True)
# ax = axs[0]
# ax.errorbar(x, y, yerr=yerr)
# ax.set_title('all errorbars')

# ax = axs[1]
# ax.errorbar(x, y, yerr=yerr, errorevery=5)
# ax.set_title('only every 5th errorbar')


# fig.suptitle('Errorbar subsampling for better appearance')

# plt.show()