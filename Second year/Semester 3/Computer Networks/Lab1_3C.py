import socket

if __name__ == "__main__":
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect(('192.168.211.1',1234))
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    try:
        m = c.recv(1024)
        m = m.decode('ascii')
        print(m)
    except socket.error as msg:
        print(msg.strerror)

    s = input("Enter string: ")
    try:
        c.send(bytes(s, 'ascii'))
        r = c.recv(1024)
        r = r.decode('ascii')
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    print(r)
    c.close()