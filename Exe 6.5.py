# Space Finder

text = "X-DSPAM-Confidence:    0.8475"
space = text.find(':')
a = text[space+2:]
val = float(a)
print(val)