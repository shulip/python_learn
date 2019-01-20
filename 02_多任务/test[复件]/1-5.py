import re

patt = '\d+\s(\w+\s)*(\w+)'

b = re.match(patt,'5621 De la Crue Boulend')

print(b.group())
