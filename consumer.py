import socket
import sys
from time import sleep

if len(sys.argv) >2 and sys.argv[2]=='--from-beginning':
    file = open(sys.argv[1]+".txt", 'r')
    for each in file:
        print (each)
    file.close()
    topic = sys.argv[1]
elif len(sys.argv) > 1 and sys.argv[1]=='--from-beginning':
    file = open('default.txt', 'r')
    for each in file:
        print (each)
    file.close()
    topic="default"
elif len(sys.argv) > 1 :
    topic = sys.argv[1]
else:
    topic = "default"
while True:
    try:
        cr = socket.socket()
        cr.connect(("127.0.0.1", 4200))
        msg = "c\t" + topic
        cr.send(msg.encode())
        while True:
            msg = cr.recv(1024).decode()
            print(msg)
            cr.send(("gotcha".encode()))
    except:
        print("CONNECTION TERMINATED. RETRYING")
        sleep(2)