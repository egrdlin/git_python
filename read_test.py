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
file_contents = file_contents.replace("\b","").replace("\t\t\t","").replace(" ","") # remove new line characters and all white spaces

file_contents = file_contents[15:]
print("after strip:\n", file_contents)

#FIXME: read the .txt and store into a tuple of list for comparison
#TODO: Try to read line by line usin for loop

