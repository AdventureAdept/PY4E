#  File Name

# Input : mbox-short.txt
# Download From: https://www.py4e.com/code3/mbox-short.txt?PHPSESSID=41016ddad74a91c038b6b58ccccb5a22 
# Expected Output Average spam confidence: 0.7507185185185187

fname = input("Enter file name: ")
fh = open(fname)
s = 0.0
count = 0

for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") :
                continue
        else:
                s = s + float(line[20:])
                count = count + 1

print("Average spam confidence:", s /count)