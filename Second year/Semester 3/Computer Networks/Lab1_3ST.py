import socket, threading, os

threads = []
client_count = 0


def timeout():
    global threads
    print("Shutting down server...")
    for t in threads:
        t.join()
    os._exit(0)


def worker(c):
    global client_count
    print('client #', client_count, 'from ', c.getpeername())
    message = 'Hello client #' + str(client_count)

    try:
        c.send(bytes(message, 'ascii'))
        st = c.recv(1024)
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    st = st.decode('ascii')
    r = ''
    for char in st:
        r = char + r
    try:
        c.send(bytes(r,'ascii'))
    except socket.error as msg:
        print(msg.strerror)

    c.close()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('192.168.211.1',1234))
        s.listen(5)
    except socket.error as msg:
        print(msg.strerror)
    timer = threading.Timer(30, timeout)
    timer.start()
    while True:
        c, addrc = s.accept()
        timer.cancel()
        timer = threading.Timer(30, timeout)
        timer.start()
        t = threading.Thread(target = worker, args = (c,))
        threads.append(t)
        client_count += 1
        t.start()
