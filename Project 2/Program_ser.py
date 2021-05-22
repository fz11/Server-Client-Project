# Fabricio Zuniga
# Project 2
# EE 3233
# Fall 2020

#!/bin/python3

# import libraries
import socket
import threading

HEADER = 1000
# Max size of message
PORT = 8888
# port number
SERVER = socket.gethostbyname(socket.gethostname())
# will get server name info
ADDR = (SERVER, PORT)
# tuple of Server name and port
FORMAT = 'utf-8'
# encoding format
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# create socket using IPv4 and streaming between client and server
server.bind(ADDR)
# defines the local port


# function to handle incoming client
def handle_client(conn, addr):
    # print(f"[NEW CONNECTION] {addr} connected.")
    print(f"connected from {SERVER}. port {PORT}")
    # print will show tuple ADDR

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # length of message will be within header size and utf-8 format
        if msg_length:
            msg_length = int(msg_length)
            # convert to integer
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                # will disconnect when message returns disconnect message

            print(f"received: {msg}")

            C_MSG = msg.upper()
            # creates all uppercase for incoming message
            if C_MSG.isupper or type(C_MSG) is int or type(C_MSG) is float:
                # to check if message is all uppercase or purely integer or float message
                print(f"sent to client: {C_MSG}")
                conn.send(f"Server sent: {C_MSG}".encode(FORMAT))
                # this will send message "sever sent {C_MSG}" back to client

    conn.close()
    # close connection


# function to start server
def start():
    server.listen()
    # server listens for a connection within local server address/port
    print("waiting for incoming connection")
    while True:
        conn, addr = server.accept()
        # server accepts connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        # each client will be handled by a thread in order to avoid the issue of
        # the client waiting for another client to disconnect in order to make a connection
        thread.start()
        # start the thread activity


start()
# call the function to begin
