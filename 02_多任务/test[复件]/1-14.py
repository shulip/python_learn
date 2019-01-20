import re

patt = '\d{4}\s(0?[1-9]|[10-12])'

dates = ['2011 01','2025 12','2001 9']

for date in dates:
    b = re.match(patt,date)
    if b:
        print(b.group())
    else:
        None
