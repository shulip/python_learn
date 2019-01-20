import re

patt = '\w+\s*\w+'

b = re.match(patt,'Zixian Wang')
c = re.match(patt,'wangxifeng')

print(b.group())
print(c.group())
