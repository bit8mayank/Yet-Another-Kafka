import socket, os
from time import time, sleep
from threading import Thread
from pprint import pprint
send = "flr"
# topic: []
consumers_data = {
    
}
# producer_data = {
# }

def handle_consumer(conn, msg):
    if msg[1] in consumers_data:
        consumers_data[msg[1]].append(conn)
    else:
        consumers_data[msg[1]] = [conn]
    pprint(consumers_data)

def handle_producer(conn, msg):
    topic_file=msg[1]+'.txt'
    if msg[1] in consumers_data:
        file = open(topic_file, 'a')
        file.write(msg[2]+'\n')
        file.close()
        # producer_data[msg[1]]=producer_data[msg[1]]+ msg[2]
        for consumer in consumers_data[msg[1]]:
            print("SENDING MESSAGE")
            try:
                consumer.send(msg[2].encode())
                print(consumer.recv(1024).decode())
            except Exception as error:
                print(error)
                consumers_data[msg[1]].remove(consumer)

    else:
        file = open(topic_file, 'w')
        file.write(msg[2]+'\n')
        file.close()
        # producer_data[msg[1]]=msg[2]
        pass
    conn.send("GOTCHA".encode())


def broker():
    print("BROKER STARTED")
    br = socket.socket()
    br.bind(("127.0.0.1", 4200))
    br.listen(100)
    while True:
        conn, addr = br.accept()
        msg = conn.recv(1024).decode().split("\t")
        if msg[0] == "p":
            print("P")
            handle_producer(conn, msg)
        elif msg[0] == "c":
            print("C")
            handle_consumer(conn, msg)

while True:
    br = socket.socket()
    br.connect(("127.0.0.1", 6969))
    br.send(send.encode())
    cmd = br.recv(1024).decode()
    if cmd == "ldr":
        print("ldr")
        send = "ldr"
        Thread(target = broker).start()
        # break
    sleep(1)

