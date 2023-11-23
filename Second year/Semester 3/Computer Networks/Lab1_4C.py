import socket
import struct

if __name__ == '__main__':
    try:
        s = socket.create_connection(('192.168.211.1', 1234))
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    try:
        m = s.recv(1024)
        m = m.decode('ascii')
        print(m)
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    n = int(input("Enter the nb of chars for the first list: "))
    l1 = []
    for i in range(0, n):
        c = input("Enter a char: ")
        l1.append(c)

    m = int(input("Enter the nb of chars for the second list: "))
    l2 = []
    for i in range(0, m):
        c = input("Enter a char: ")
        l2.append(c)

    try:
        s.send(struct.pack('!I', n))
        for c in l1:
            s.send(bytes(c,'ascii'))
        s.send(struct.pack('!I', m))
        for c in l2:
            s.send(bytes(c, 'ascii'))

    except socket.error as msg:
        print(msg.strerror)
        exit(-1)
    l3=[]
    try:
        for i in range(0, n+m):
            ch = s.recv(1)
            ch = ch.decode('ascii')
            l3.append(ch)
        print("The sorted list is: ", l3)
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    s.close()
