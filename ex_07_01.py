# Keep prompting user input
while True:
    try:
        filename = input("Enter the file name: ")
        fhand = open(filename)
    except Exception as e:
        print("File can not be opened: ", filename)
        continue
    break

# for i in fhand:
#     print(i)

context = fhand.read()
print((context.upper()).rstrip())