import re

patt = '[+|-]?\d+\.?\d*'
nums =['5695','884.542','+848.84']

for num in nums:
    b = re.match(patt,num)
    if num:
        print(b.group())
    else:
        None
