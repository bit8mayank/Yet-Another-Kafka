import socket
import sys
from time import sleep
if len(sys.argv) > 1:
    topic = sys.argv[1]
else:
    topic = "default"
while True:
    msg = "p\t" + topic + "\t" + input("Enter the message: ")
    try:
        pr = socket.socket()
        pr.connect(("127.0.0.1", 4200))
        pr.send(msg.encode())
        reply = pr.recv(1024).decode()
        print(reply)
        pr.close()
    except:
        sleep(2)
        pr = socket.socket()
        pr.connect(("127.0.0.1", 4200))
        pr.send(msg.encode())
        reply = pr.recv(1024).decode()
        print(reply)
        pr.close()