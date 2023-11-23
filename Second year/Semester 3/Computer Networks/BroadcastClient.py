import socket
from time import sleep

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

    while True:
        client.sendto(b'Hi',('255.255.255.255',7777))
        sleep(2)
