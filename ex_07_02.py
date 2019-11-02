# Keep prompting user input
print('\033c') # clear the screen

while True:
    try:
        filename = input("Enter the file name: ")
        fhand = open(filename)
    except Exception as e:
        print("File can not be opened: ", filename)
        continue
    break

extracted_data = 0.0
sum_data = 0.0
count_data = 0
count_subject = 0
for line in fhand: 
    if "X-DSPAM-Confidence" in line:
        index = line.find(":")
        extracted_data = float(line[index+1:])
        sum_data = sum_data + extracted_data
        count_data +=1
    # print("Extracted Data: ",extracted_data)
    line = line.lower()
    if line.startswith("subject"):
        count_subject +=1
mean_data = sum_data / count_data
print("Average Spam Confidence: ", mean_data)
print("Subject Lines: ", count_subject)
print("======================================COMPLETE======================================")

