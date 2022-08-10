# sockets programming
# basic use of networking

import socket
import threading

# handling seperate messages using Thread
# THREADS ARE USED TO SEPERATE CODES OUT so that the functions gets completed without waiting for other processes to finish It basically handles message handling........
# The client dosnt need to wait for the other client to complete its process

HDR = 64  # bytes can be changed if large size
PORT = 5050
# or else you can use this  it shows the ip address of the pc SERVER = "192.168.0.102"
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISSCONECT_MESSAGE = "DISCONNECT"
# socket.AF_INET and ___6 is for IPV6 is Family
# SOCK_STREAM is Type means Streaming over the data
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
server.bind(ADDRESS)


def client_communication(connection, address):
    print(f"NEW CONNECTION {address} succesfull. \n")

    successfull = True
    while successfull:
        # usage of message protocol limited size in recv(limited size)
        msg_length = connection.recv(HDR).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = connection.recv(msg_length).decode(FORMAT)
            if msg == DISSCONECT_MESSAGE:
                successfull = False

            print(f"[{address}] {msg}")

    connection.close()


def start():
    # inside we are creating a server to start listening to connections and handling the connection to the client_communication for running in new thread
    server.listen()
    print(f"[Listening] Server on IP {SERVER}")
    while True:
        # accepting a new connection and storing its IP address and port it came from client
        connection, address = server.accept()
        thread = threading.Thread(target=client_communication,
                                  args=(connection, address))
        thread.start()
        # active count -1 means if 2 threads are running remove one and display the one active connection
        print(f"Active connections {threading.active_count() - 1}")


print("Server is starting..............")
start()
