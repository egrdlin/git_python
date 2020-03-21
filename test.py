# quick program to test python read by size functionality

fhand = open("Amendment.txt","r")
print(fhand.read(10))
print("=BREAK=")
print(fhand.read(10))
print("=BREAK=\n",fhand.read(20))
