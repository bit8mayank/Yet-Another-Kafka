import socket, os
from time import time, sleep
zk = socket.socket()
zk.bind(("127.0.0.1", 6969))
zk.listen(10)
lp = time() - 2
while True:
    conn, addr = zk.accept()
    msg = conn.recv(1024).decode()
    if msg == "ldr":
        lp = time()
        conn.send("flr".encode())
    else:
        if time() - lp > 2:
            conn.send("ldr".encode())
            lp = time()
        else:
            conn.send("flr".encode())
