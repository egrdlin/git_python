import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

img = urllib.request.urlopen("http://data.pr4e.org/cover3.jpg")
fhand = open("cover3.jpg", "wb")
size = 0 

while True:
    info = img.read(100000)
    if len(info)<1 : break
    size = size + len(info)
    fhand.write(info)

print("Write Completed!", size, " characters copied!")
fhand.close()
