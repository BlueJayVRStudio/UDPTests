import os
import socket
import time

import struct

class Vector3:
    def __init__(self, _x, _y, _z):
        self.x = _x
        self.y = _y
        self.z = _z
    

class Message:
    def __init__(self, _name, _position):
        self.name = _name
        self.position = _position

# value = 25788.567777778888
# _bytes = struct.pack("d", value)
# # ba = bytearray(struct.pack("f", value))  

# print(value)
# toSend = ""
# for i in _bytes:
#     toSend += chr(i)
# print(toSend)
# print(type(toSend))
# toSend = toSend.encode()

# byteArray = []
# for i in toSend.decode():
#     byteArray.append(ord(i))
# ba = bytearray(byteArray)
# print(ba)
# print(type(struct.unpack("d", ba)[0]))
# print(struct.unpack("d", ba)[0])

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVER_ADDR = os.getenv("SERVER_ADDR")
target_host = SERVER_ADDR
target_port = 1234

server_ip = '0.0.0.0'  
server_port = 1234

udp_socket.bind((server_ip, server_port))

message = "Hello, UDP Server!"

t1 = time.time()
udp_socket.sendto(message.encode(), (target_host, target_port))
data, addr = udp_socket.recvfrom(1024)
print((time.time()-t1)*1000)
print(data.decode())

udp_socket.close()