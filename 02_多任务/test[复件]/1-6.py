import re

patt = '(^www|http)://(\w+\.)*(edu|net|com$)'
letters = ['www://www.yahoo.com','http://www.foothill.edu']
for letter in letters:
    b = re.match(patt,letter)
    if b:
        print(b.group())
    else:
        None


