inp = input('Enter file name: ')
fhand = open(inp)

import re

lst = list()
for line in fhand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    for num in x:
        lst.append(int(num))
        
print(sum(lst))