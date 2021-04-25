import socket
import pickle
import struct

UDP_IP = socket.gethostname() # returns the IP of this device
UDP_PORT = 5005  # port number
print(UDP_IP)
# initialize UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind socket to address
sock.bind(('192.168.1.4', UDP_PORT))

print("waiting for incoming messages...")
print("press CTRL+C to exit")

while True:
    data, addr = sock.recvfrom(12)  # receive data with certain buffer size

    print(f"received following message: {data.decode('utf-8')} from {addr}")  # decode incoming message


    sock.sendto("message received!".encode('utf-8'), (addr[0], addr[1]))  # send response to client

