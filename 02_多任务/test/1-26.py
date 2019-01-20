import re

patt = '\w+@(\w+.)+\w+'
datas = []

filename = 'redata.txt'
with open(filename,'r') as f:
    lines = f.readlines()

for line in lines:
    b = re.sub(patt,'wzx569159845@live.com',line)
    datas.append(b)

print(datas)

with open(filename,'w') as f:
    for data in datas:
        f.write(data+'\n')
