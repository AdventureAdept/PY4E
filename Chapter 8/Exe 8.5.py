# File Sorter
# Input: mbox-short.txt
# Download: https://www.py4e.com/code3/mbox-short.txt?PHPSESSID=994891862bf5a8324450d19d922b58a7
"""

 Expected Output: stephen.marquard@uct.ac.za
 louis@media.berkeley.edu
 qian@umich.edu
 rjlowe@iupui.edu
 zqian@umich.edu
 rjlowe@iupui.edu
 cwen@iupui.edu
 cwen@iupui.edu
 gsilver@umich.edu
 gsilver@umich.edu
 qian@umich.edu
 gsilver@umich.edu
 wagnermr@iupui.edu
 zqian@umich.edu
 antranig@caret.cam.ac.uk
 gopal.ramasammycook@gmail.com
 david.horwitz@uct.ac.za
 david.horwitz@uct.ac.za
 david.horwitz@uct.ac.za
 avid.horwitz@uct.ac.za
 stephen.marquard@uct.ac.za
 louis@media.berkeley.edu
 louis@media.berkeley.edu
 ray@media.berkeley.edu
 cwen@iupui.edu
 wen@iupui.edu
 cwen@iupui.edu
 There were 27 lines in the file with From as the first word

"""

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
data=[]
for each in fh:
    if each.startswith("From") and len(each.split())>2:
        temp=each.split()
        data.append(temp[1])
for each in data:
    print(each)
print("There were", len(data), "lines in the file with From as the first word")