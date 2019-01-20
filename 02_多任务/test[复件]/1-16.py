from random import randrange,choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com','edu','net','gov')
filename = 'redata.txt'
f = open(filename,'w')

for i in range(randrange(5,11)):
    dtint = randrange(maxsize)/1000000000 #pick date
    dtstr = ctime(dtint)                  #date str
    llen = randrange(4,8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen,13)
    dom = ''.join(choice(lc) for j in range(dlen))
    data='%s::%s@%s.%s::%d-%d-%d'% (dtstr,login,dom,choice(tlds),dtint,llen,dlen)
    f.write(data+'\n')

f.close()