import socket, threading, os
import struct

threads = []
client_count = 0


def timeout(s):
    global threads
    print("Shutting down...")
    for t in threads:
        t.join()
    s.close()
    os._exit(0)


def worker(c):
    msge = "Hello client #" + str(client_count)
    print("Connected client #", client_count, " from ", c.getpeername())
    try:
        c.send(bytes(msge, 'ascii'))
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    try:
        n = c.recv(4)
        n = struct.unpack('!I',n)[0]
        l1 = []
        for i in range(0,n):
            ch = c.recv(1)
            ch = ch.decode('ascii')
            l1.append(ch)
        m = c.recv(4)
        m = struct.unpack('!I', m)[0]
        l2 = []
        for i in range(0, m):
            ch = c.recv(1)
            ch = ch.decode('ascii')
            l2.append(ch)
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    # merge sort
    l3 = []
    i = 0
    j = 0
    while i < n or j < m:
        if i >= n:
            for x in range(j,m):
                l3.append(l2[x])
            j = m
        elif j >= m:
            for x in range(i,n):
                l3.append(l1[x])
            i = n
        else:
            if l1[i] > l2[j]:
                l3.append(l2[j])
                j += 1
            else:
                l3.append(l1[i])
                i += 1

    try:
        for ch in l3:
            c.send(bytes(ch, 'ascii'))
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    c.close()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('192.168.211.1', 1234))
        s.listen(5)
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    timer = threading.Timer(30, timeout, args = (s,))
    timer.start()
    while True:
        c, addr = s.accept()
        client_count += 1
        t = threading.Thread(target=worker, args=(c,))
        threads.append(t)
        timer.cancel()
        timer = threading.Timer(30, timeout, args = (s,))
        timer.start()
        t.start()

