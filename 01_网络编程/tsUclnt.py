from socket import *

HOST = gethostname()
PORT = 21567
BUFSIZ =1024
ADDR = (HOST,PORT)

udpCliScok = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliScok.sendto(data.encode(),ADDR)
    data,ADDR = udpCliScok.recvfrom(BUFSIZ)
    data = data.decode()
    if not data:
        break
    print(data)

udpCliScok.close()

