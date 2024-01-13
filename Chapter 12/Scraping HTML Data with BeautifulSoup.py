# Scraping HTML Data with BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter: ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

numlist = list()
tags = soup("span")

for tag in tags:
    lines = tag
    for line in lines:

        number = re.findall("[0-9]+", line)
        for x in number:

            numlist.append(int(x))

print(sum(numlist))