import socket, struct

if __name__ == '__main__':
    try:
        s = socket.create_connection(('172.21.160.1', 1234))
    except socket.error as msg:
        print("Error: ", msg.strerror)

    n = int(input('Enter number of elements: '))
    # pack the value of n as a short int (16 bits) in network representation
    res = s.send(struct.pack("!H", n))

    for i in range(0, n):
        x = int(input("Enter element: "))
        res = s.send(struct.pack("!H", x))

    data = s.recv(4)
    data = struct.unpack('!H', data)[0]
    print("The sum is: ", data)
    s.close()


