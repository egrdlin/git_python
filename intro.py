# Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function.

# For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list.

# When the program completes, sort and print the resulting words in alphabetical order.

while True:
    try:
        filename = input("Enter the file name: ")
        fhand =  open(filename)
    except Exception as e:
        print("File ' ",filename, "' couldn't be found. Retry again")
    break

text_str = fhand.read() # txt to string
text_list =text_str.split() # string to list

user_list = list() # declare an user list
# user_list.extend(["soft", "Juliet", "grief"]) # debug purpose

for word in text_list:
    if word in user_list:
        # print("Existed word: ", word) # debug purpose
        continue
    else:
        user_list.append(word)

user_list.sort()    # sort the user list in order
print(user_list) 



    