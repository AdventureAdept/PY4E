name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()                                    
lst = []                                           

for line in handle: 
    words = line.split()
    if len(words) > 2 and words[0] == 'From':       
        hr = words[5].split(':')                   
        count[hr[0]] = count.get(hr[0], 0) + 1    
    else:
        continue

for k,v in count.items():                           
    lst.append((k,v))                              

lst.sort()                                     
for k,v in lst:                                   
    print(k,v)