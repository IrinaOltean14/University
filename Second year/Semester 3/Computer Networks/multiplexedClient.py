import sys
import socket
import threading
import time


def receive_server_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode("ascii")
            print(data)
        except ConnectionAbortedError:
            print("Server closed the connection.")
            break

def get_input_and_send(client_socket):
    while True:
        try:
            data = input()
            client_socket.send(bytes(data, "ascii"))
            if data == "QUIT":
                client_socket.close()
                break
        except ConnectionAbortedError:
            print("Server closed the connection.")
            break

if __name__ == "__main__":
    port = 1234
    IP_address = '127.0.0.1'

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP_address, port))

    # Create threads for receiving messages and getting input
    receive_thread = threading.Thread(target=receive_server_messages, args=(client_socket,))
    input_thread = threading.Thread(target=get_input_and_send, args=(client_socket,))

    # Start the threads
    receive_thread.start()
    input_thread.start()

    # Wait for both threads to finish
    receive_thread.join()
    input_thread.join()