import struct
import socket
import threading
import os

peers = []
finished = False
my_lock = threading.Lock()


def send_messages(c, server):
    while True:
        m = input()
        len_m = len(m)
        if m == 'QUIT':
            try:
                server.send(bytes(m,'ascii'))
            except socket.error as msg:
                print(msg.strerror)
                exit(-1)
            os._exit(0)
        else:
            print('Sending message to clients')
            try:
                (i,p) = c.getsockname()
                for adr in peers:
                    ip = adr[0]
                    port = adr[1]
                    if port != p:
                        c.sendto(struct.pack('!I', len_m),(ip,port))
                        c.sendto(bytes(m,'ascii'), (ip,port))
            except socket.error as msg:
                print(msg.strerror)
                exit(-1)


def get_message(c):
    while True:
        try:
            len_m, addr = c.recvfrom(4)
            len_m = struct.unpack('!I', len_m)[0]
            m = c.recv(len_m)
            m = m.decode('ascii')
            print(m)
        except socket.error as msg:
            print(msg.strerror)
            exit(-1)


def changes(old, new):
    for p in old:
        if p not in new:
            print('Client ', p, ' has disconnected')
    for p in new:
        if p not in old:
            print('Client ', p, ' has connected')


def get_connected_clients(s):
    global peers
    while True:
        new_peers = []
        try:
            n = s.recv(4)
            n = struct.unpack('!I', n)[0]
            for i in range(0,n):
                len_ip = s.recv(4)
                len_ip = struct.unpack('!I', len_ip)[0]
                ip = s.recv(len_ip)
                ip = ip.decode('ascii')
                port = s.recv(4)
                port = struct.unpack('!I', port)[0]
                new_peers.append((ip,port))
        except socket.error as msg:
            print(msg.strerror)
            exit(-1)
        changes(peers, new_peers)
        my_lock.acquire()
        peers = new_peers
        my_lock.release()
        print('New list of clients: ', peers)


if __name__ == '__main__':
    # create TCP socket to connect to the server
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect(('127.0.0.1',7000))
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    try:
        len_m = server.recv(4)
        len_m = struct.unpack('!I', len_m)[0]
        m = server.recv(len_m)
        print(m.decode('ascii'))
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    get_clients_thread = threading.Thread(target = get_connected_clients, args = (server,))
    get_clients_thread.start()
    (i,port1) = server.getsockname()
    # create socket for UDP communicating
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        c.bind(('0.0.0.0', port1))
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    send_m = threading.Thread(target = send_messages, args=(c,server))
    recv_m = threading.Thread(target = get_message, args = (c,))
    send_m.start()
    recv_m.start()
