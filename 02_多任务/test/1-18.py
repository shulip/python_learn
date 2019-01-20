import re

patt = '\w{3}\s\w{3}\s[1-3]\d\s[0-2]\d:\d{2}:\d{2}'

filename = 'redata.txt'
with open(filename,'r') as f:
    lines = f.readlines()

for line in lines:
    b = re.match(patt,line)

    if b:
        print(b.group())
    else:
        None
