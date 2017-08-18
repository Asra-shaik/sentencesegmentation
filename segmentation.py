from urllib.request import urlopen
#urlopen is used to open a remote object across a network and read it.
#urllib contains func for requesting data across web
from bs4 import BeautifulSoup
#bs is used for pulling data from html/xml files
url="https://en.wikipedia.org/wiki/Malayalam"
html=urlopen(url).read()#read source code
soup=BeautifulSoup(html)
#Now you have to pass something to BeautifulSoup to create a soup object.
#That could be a document or an URL.(obj creation)
for script in soup(["script","style"]):
    script.extract()
text=soup.get_text()#text format
lines=(line.strip() for line in text.splitlines())#lines/space remove
chunks=(phrase.strip() for line in lines for phrase in line.split(" "))#doubt
text='\n'.join(chunk for chunk in chunks if chunk)
print(text)
#http://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python
#.strip() removes all whitespace at the start and end, including spaces, tabs, newlines
# splitlines() returns a list with all the lines in string, optionally including the line breaks
