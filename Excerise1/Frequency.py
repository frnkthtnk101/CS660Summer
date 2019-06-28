import string
import sys

argc = len(sys.argv)
if argc == 1:
    print("usage:  freq.pl file")
    exit()
elif argc == 2:
    filename = sys.argv[1]
    infile = open(filename,'r')


freq = {}
count = 0
for c in string.ascii_lowercase:
    freq[c] = 0

for line in infile:
    for c in line.lower():
        if c.isalpha():
            freq[c] = freq[c] + 1
            count = count + 1


keys = sorted(freq)
for c in keys:
  print(c,float(freq[c])/count)
