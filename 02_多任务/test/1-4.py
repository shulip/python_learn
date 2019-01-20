import re

patt = '[_a-zA-z][\w_]+'
b = re.match(patt,'ads_213')
c = re.match(patt,'_we2')
d = re.match(patt,'12weq')
print(b.group())
print(c.group())
print(d.group())
