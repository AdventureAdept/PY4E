# Counting Word Frequency using a Dictionary
# Input: mbox-short.txt
# Download From: https://www.py4e.com/code3/mbox-short.txt?PHPSESSID=994891862bf5a8324450d19d922b58a7
# Expected Output: cwen@iupui.edu 5

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)


authors = dict()

for line in handle:
    line.strip()
    if not line.startswith("From "): continue
    words = line.split()
    authors[words[1]] = authors.get(words[1],0)+1

count = None
largest_author = None

for key in authors:
    if count is None: count = authors[key]

    if count < authors[key]:
        count = authors[key]
        largest_author = key

print(largest_author, count)