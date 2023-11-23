import select
import struct
import socket

addresses = dict()


def send_clients():
    global addresses
    for c in addresses.keys():
        try:
            c.send(struct.pack('!I', len(addresses)))
            for adr in addresses.values():
                ip = adr[0]
                port = adr[1]
                c.send(struct.pack('!I', len(ip)))
                c.send(bytes(ip,'ascii'))
                c.send(struct.pack('!I', port))
        except socket.error as msg:
            print(msg.strerror)
            exit(-1)


if __name__ == '__main__':
    # create TCP socket for client connection
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0',7000))
        server.listen(10)
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)

    master = [server]
    while True:
        ready_to_read, _, _ = select.select(master, [], [])
        for s in ready_to_read:
            if s is server:
                # this means a new client connected to the server
                client, addr = server.accept()
                print('New client from ', addr)
                master.append(client)
                m = 'Welcome!'
                try:
                    client.send(struct.pack('!I', len(m)))
                    client.send(bytes(m,'ascii'))
                except socket.error as msg:
                    print(msg.strerror)
                    exit(-1)
                #addresses[client] = (addr[0], port)
                addresses[client] = addr
                send_clients()
            else:
                master.remove(s)
                del addresses[s]
                send_clients()
                s.close()