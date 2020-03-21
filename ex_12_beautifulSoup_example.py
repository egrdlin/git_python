
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')
url_list = list()

tags = soup("a")
for tag in tags:
    print("\n=======================================================")
    print("Tag:", tag)
    print("URL: ",tag.get("href", None)) #access all tags <a> with href
    url_list.append(tag.get("href", None))
    print("Contents:",tag.contents[0])
    print("Attrs: ", tag.attrs)
    print("=======================================================\n")

print(url_list)