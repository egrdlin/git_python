import re

while True:
    try:
        filename = input("Enter the file name:")
        if len(filename) <1 : filename = "mbox.txt"
        fhand = open(filename)
        print("Opening file '{}'...\n".format (filename))
    except Exception as e:
        print("Can't open the file")
        continue
    break


total = 0
count = 0
for line in fhand:
    line = line.rstrip()
    search_result = re.search('^New Revision', line) # true or false
    if search_result:
        #print(line)
        res = [int(i) for i in line.split() if i.isdigit()]
        res = sum(d * 10**i for i, d in enumerate(res[::-1]))  
        total = total+res
        count +=1
        # print(res)
print(total/count)
#TODO: Capture the number from string