# File Name Sorter
# Input: romeo.txt
# Download: https://www.py4e.com/code3/romeo.txt?PHPSESSID=35ed32e4a3d2c1cf2227af04512951e4
# Expected Output: ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder'] 

fname = input("Enter file name: ")
fh = open(fname)
data=[]
for each in fh:
    words=each.split()
    for word in words:
        if word not in data:
            data.append(word)
print(sorted(data))