#  Rewrite the program that prompts the user for a list of numbers and prints 
# out the maximum and minimum of the numbers at the end when the user enters 
# "done". Write the program to store the numbers the user enters in a list and 
# use the max() and min() functions to compute the maximum and minimum numbers 
# after the loop completes.

user_list = list()
while True:
    user_input = input("Enter a number: ")
    if user_input.lower() == "done": break # if user enters "done", break will take the control out of loop
    try:
        user_input = int(user_input) # string to int
        user_list.append(user_input) # add int to the list
    except Exception as e:
        print("Unable to be stored") # print error
        continue
        
print("The maximum value entered: ",max(user_list), "The minimum value entered: ", min(user_list)) # print desired max and min val