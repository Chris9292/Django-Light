import socket
import sys
import pickle

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # initialize UDP socket
address = ("192.168.1.130", 11000)  # receiver's address --> (IP, PORT)


while True:
    message = bytes(input("Enter message for the server: "), 'utf-8')  # input a string from user and convert to bytes

    # print user message and memory size
    print(message)
    print(sys.getsizeof(message))

    # send serialized byte-object to server
    socket.sendto(message, address)

    # wait for server response
    data, addr = socket.recvfrom(1024)

    # print received data
    print(f"Message from IP: {addr[0]} and PORT: {addr[1]} --> {data.decode('utf-8')}")
