import threading, struct, socket, os

threads = []
client_count = 0
e = threading.Event()
w = threading.Event()
e.clear()
w.clear()
my_lock = threading.Lock()
r = []
ending = False
end_thread = -1

def worker(c):
    global e, client_count,r, ending, end_thread
    m = 'Welcome client #' + str(client_count)
    print('Connected client #',client_count, ' from ', c.getpeername())
    try:
        c.send(bytes(m,'ascii'))
    except socket.error as msg:
        print("Error: ", msg.strerror)
        exit(-1)

    l = []
    try:
        n = c.recv(4)
        n = struct.unpack('!I', n)[0]
        for i in range(0,n):
            x = c.recv(4)
            x = struct.unpack('!I', x)[0]
            l.append(x)
    except socket.error as msg:
        print("Error: ", msg.strerror)
        exit(-1)

    my_lock.acquire()
    i = 0
    j = 0
    p = []
    while i < len(l) or j < len(r):
        if i >= len(l):
            p.append(r[j])
            j += 1
        elif j >= len(r):
            p.append(l[i])
            i += 1
        elif l[i] < r[j]:
            p.append(l[i])
            i += 1
        else:
            p.append(r[j])
            j += 1
    r = p
    my_lock.release()

    if n == 0:
        ending = True
        end_thread = threading.get_ident()

    if ending:
        if end_thread == threading.get_ident():
            e.set()
            w.set()
    w.wait()
    try:
        c.send(struct.pack('!I', len(r)))
        for x in r:
            c.send(struct.pack('!I', x))
    except socket.error as msg:
        print("Error: ", msg.strerror)
        exit(-1)
    c.close()


def end():
    global e, threads
    e.wait()
    for t in threads:
        t.join()
    s.close()
    os._exit(0)


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0',1234))
        s.listen(5)
    except socket.error as msg:
        print("Error: ", msg.strerror)
        exit(-1)

    q = threading.Thread(target = end, daemon = True)
    q.start()
    while True:
        c, addr = s.accept()
        t = threading.Thread(target = worker, args = (c,))

        client_count += 1
        threads.append(t)
        t.start()
