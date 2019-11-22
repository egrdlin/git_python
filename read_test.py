while True:
    try: 
        fhand = open("letter-frequency.txt")
    except Exception as e:
        print("File cannot be opened. Try again!")
        continue
    break


file_contents = fhand.read() # read the whole file
file_contents = file_contents.strip()
file_contents = file_contents.replace("\t\t"," ").replace("\n","\t")
file_contents = file_contents[20:]
print(file_contents)
#FIXME: construct dictionary --> sort dictionary --> Export dictionary -->

# file_contents = file_contents[20:]
# print("after strip:\n", file_contents)
# file_contents = file_contents.replace("\t","").replace("\t\t\t","").replace(" ","").replace("\n","") # remove new line characters and all white spaces

# char_index = list()
# file_contents_list = list()

# for ind, char in enumerate(file_contents):
#     if char.isalpha():
#         # print(char, ind)
#         char_index.append(ind)
# print(char_index)

# # get the frequency into a list
# for i in range(0, len(char_index)):
#     if i+1 != len(char_index):
#         first_index = char_index[i]
#         second_index = char_index[i+1]
#         print(file_contents[first_index+1:second_index])
#     else:
#         last_index = char_index[-1]
#         print(file_contents[(last_index+1):])

# #TODO: sort list in alphabetic order 

