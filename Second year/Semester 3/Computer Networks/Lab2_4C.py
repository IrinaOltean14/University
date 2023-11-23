import struct, socket

if __name__ == '__main__':
    try:
        c = socket.create_connection(('127.0.0.1',1234))
    except socket.error as msg:
        print("Error: ", msg.strerror)
        exit(-1)

    try:
        m = c.recv(1024)
        print(m.decode('ascii'))
    except socket.error as msg:
        print("Error: ", msg.strerror)
        exit(-1)

    n = int(input("Enter the number of elements: "))
    l = []
    for i in range(0,n):
        x = int(input("Enter number: "))
        l.append(x)
    try:
        c.send(struct.pack('!I', n))
        for x in l:
            c.send(struct.pack('!I', x))
    except socket.error as msg:
        print("Error: ", msg.strerror)
        exit(-1)

    r = []
    try:
        m = c.recv(4)
        m = struct.unpack('!I', m)[0]
        for i in range(0,m):
            x = c.recv(4)
            x = struct.unpack('!I', x)[0]
            r.append(x)
    except socket.error as msg:
        print("Error: ", msg.strerror)
        exit(-1)

    print("The sorted array is: ", r)
    c.close()