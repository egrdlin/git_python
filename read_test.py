while True:
    try: 
        fhand = open("letter-frequency.txt")
    except Exception as e:
        print("File cannot be opened. Try again!")
        continue
    break


file_contents = fhand.read() # read the whole file
print(file_contents)
file_contents = file_contents.strip()
file_contents = file_contents.replace("\t","").replace("\t\t\t","").replace(" ","").replace("\n","") # remove new line characters and all white spaces

file_contents = file_contents[15:]
print("after strip:\n", file_contents)

char_index = list()
file_contents_list = list()

for ind, char in enumerate(file_contents):
    if char.isalpha():
        # print(char, ind)
        char_index.append(ind)
print(char_index)

# for i in range(0,len(char_index)): # get all but last percentage
#     current_ind = char_index[i-1]
#     next_ind = char_index[i]
#     temp = file_contents[current_ind+1:next_ind]
#     print(temp)

# start = char_index[len(char_index)-1]
# last_val = file_contents[start+1:] # get last value
# print(last_val)

#TODO: sort list in alphabetic order 

