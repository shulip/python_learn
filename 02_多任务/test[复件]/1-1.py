import re

patt = '[hb][aiu]t'

b = re.match(patt,'bat')
c = re.match(patt,'bit')
d = re.match(patt,'but')
e = re.match(patt,'hat')
f = re.match(patt,'hit')
g = re.match(patt,'hut')
print(b.group())
print(c.group())
print(d.group())
print(e.group())
print(f.group())
print(g.group())
