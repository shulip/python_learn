import re

patt = '([0-9]{4}-?[0-9]{6}-?[0-9]{5})|([0-9]{4}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4})'

numbers = ['6217-7700-0408-6025','6217-856984-89624','625414532589541','5896325559632145']

for number in numbers:
    n = re.match(patt,number)
    if n:
        print(n.group())
    else:
        None
