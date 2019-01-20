import re

patt = 'Mon|Tue|Wed|Thu|Fri|Sat|Sun'
count = [0,0,0,0,0,0,0]

filename = 'redata.txt'
with open(filename,'r') as f:
    lines = f.readlines()

def count_week(b):
    if b.group()=='Mon':
        count[0]+=1
    elif b.group()=='Tue':
        count[1]+=1
    elif b.group()=='Wed':
        count[2]+=1
    elif b.group()=='Thu':
        count[3]+=1
    elif b.group()=='Fri':
        count[4]+=1
    elif b.group()=='Sat':
        count[5]+=1
    elif b.group()=='Sun':
        count[6]+=1
    else:
        None

for line in lines:
    b = re.search(patt,line)
    count_week(b)

print(count)
