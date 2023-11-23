import socket, struct, random
import threading, time
threads = []
client_count = 0
st = 1
dr = 10000
random.seed()
my_num = random.randint(st,dr)
print("Server number: ", my_num)
client_guessed = False
winner = -1
my_lock = threading.Lock()
e = threading.Event()
e.clear()


def worker(c):
    global my_lock, client_guessed, my_num, winner, client_count, e
    my_id = client_count
    print('client #', client_count, 'from: ', c.getpeername(), c)
    message = 'Hello client #' + str(client_count) + ' ! You are entering the number guess competion now !'
    c.sendall(bytes(message, 'ascii'))

    while not client_guessed:
        try:
            nb = c.recv(4)
            nb = struct.unpack('!I', nb)[0]
            if nb > my_num:
                c.send(b'S')
            if nb < my_num:
                c.send(b'H')
            if nb == my_num:
                my_lock.acquire()
                client_guessed = True
                winner = threading.get_ident()
                my_lock.release()
        except socket.error as msg:
            print('Error:', msg.strerror)
            break

    if client_guessed:
        if threading.get_ident() == winner:
            c.sendall(b'G')
            print('We have a winner', c.getpeername())
            print("Thread ", my_id, " winner")
            e.set()
        else:
            c.sendall(b'L')
            print("Thread ", my_id, " looser")
    time.sleep(1)
    c.close()
    print("Worker Thread ", my_id, " end")



def resetSrv():
    global my_lock, client_guessed, winner, my_num, threads, e , client_count
    while True:
        e.wait()
        for t in threads:
            t.join()
        print("all threads are finished now")
        e.clear()
        my_lock.acquire()
        threads = []
        client_guessed = False
        winner = -1
        client_count = 0
        my_num = random.randint(st,dr)
        print("Server number: ", my_num)
        my_lock.release()



if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0',1234))
        s.listen(5)
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    t = threading.Thread(target = resetSrv, daemon=True)
    t.start()
    while True:
        c, addr = s.accept()
        t = threading.Thread(target = worker, args = (c,))
        threads.append(t)
        client_count += 1
        t.start()