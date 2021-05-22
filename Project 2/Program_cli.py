# Fabricio Zuniga
# Project 2
# EE 3233
# Fall 2020

#!/bin/python3

# import library
import socket

HEADER = 1000
# message size 1KB
PORT = 8888
# port is 8888
FORMAT = 'utf-8'
# encoding format
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
# will get local server name
ADDR = (SERVER, PORT)
# tuple of server and port

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client sets up socket under IPv4 connection and incoming connection between server


def send(msg):
    message = msg.encode(FORMAT)
    # will encode input message to utf-8 format
    msg_length = len(message)
    # get length of message
    send_length = str(msg_length).encode(FORMAT)
    # format to utf 8 by converting msg_length to string first
    send_length += b' ' * (HEADER - len(send_length))
    # send length will fill spaces to make it to size 1KB
    # b is byte format, ' ' is space and header - len(send_length) will determine how many white spaces to add
    client.send(send_length)
    client.send(message)
    # send to server both message and message length
    print(client.recv(2048).decode(FORMAT))
    # Receive the length of the message sent from server to client


def conn(usr):
    if usr == "localhost" or usr == "Localhost":
        # user must input local host in order to connect with server, otherwise client will not connect
        # if condition statement fails: will give error and exit program
        print(f"trying to connect to localhost, port {PORT}")
        try:
            client.connect(ADDR)
            print("connected")
            # client establishes connection based on server name and port
            while True:
                upper_message = input()
                send(upper_message)
                # user gives input message to be sent to server

        except Exception as e:
            print("connection to server failed.")
            # if connection fails

    else:
        print("connection unavailable")


print("Enter IP to connect: ")
IP = input()
conn(IP)
# send user input to conn function
