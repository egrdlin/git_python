# Use find and string slicing to extract the portion of the string after the colon 
# character and then use the float function to convert the extracted string into a floating point number

data = "X-DSPAM-Confidence:0.8475"
index = data.find(":")
print(index)

extracted_data = float(data[index+1:])
print("Extracted data: ", extracted_data)