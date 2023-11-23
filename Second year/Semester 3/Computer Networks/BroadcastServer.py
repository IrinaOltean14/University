import socket
from time import sleep

if __name__ == "__main__":
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    c.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    c.bind(('0.0.0.0',7777))

    while True:
        m,a = c.recvfrom(1024)
        print(m)
        sleep(2)