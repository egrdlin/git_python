# Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the 
# letters a-z. Find text samples from several different languages and see how letter frequency 
# varies between languages
import time
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

# for letter in ascii_lowercase: # counts letter frequency
#     if letter in letter_list:
#         print(letter)
#         continue
# // TODO: figure out a way to count the letter to 0 if they never appeared in the text

for letter in letter_list:
    # counts[letter] = counts.get(letter, 0) + 1
    print(letter)

        
            

        
          
        
        

print("dictionary counts: ", counts)

counts_list = sorted(counts.items()) # items() converts the dictionary to list, which allows sorted()
# print("list of counts: ", counts_list)

# for key,val in counts_list:
    # print(key,val)

