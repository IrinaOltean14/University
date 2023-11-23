import socket, struct, threading, os

nb_clients = 0
threads = []


def timeout_action():
    print("No client has connected in 10 seconds. Shutting down server...")
    for t in threads:
        t.join()
    os._exit(0)


def calculate_sum(cs):
    try:
        n = client_socket.recv(4)
        n = struct.unpack('!H', n)[0]
    except socket.error as msg:
        print(msg.strerror)
    suma = 0
    for i in range(0, n):
        try:
            x = client_socket.recv(4)
            x = struct.unpack('!H', x)[0]
        except socket.error as msg:
            print(msg.strerror)
            continue
        suma += x
    client_socket.send(struct.pack('!H', suma))
    client_socket.close()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('172.21.160.1',1234))
        s.listen(5)
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)
    timer = threading.Timer(10, timeout_action)
    timer.start()
    while True:
        client_socket, addr = s.accept()
        print("New client connected")
        t = threading.Thread(target=calculate_sum, args = (client_socket,))
        threads.append(t)
        nb_clients += 1
        t.start()
        timer.cancel()
        timer = threading.Timer(10, timeout_action)
        timer.start()