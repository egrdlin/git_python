import urllib.request, urllib.parse, urllib.error
import re

url = input("Enter -")
html = urllib.request.urlopen(url).read()

# search_expression = "href=\"(http://.*?" #start with string href="(http:// with zero or more occurances, non greedy
# links = re.findall(search_expression, html)

html = urllib.request.urlopen(url).read()
links = re.findall("href=\"(http://.*?" ,html)


for link in links:
    print(link.decode())