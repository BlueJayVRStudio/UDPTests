import os
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVER_ADDR = os.getenv("SERVER_ADDR")
target_host = SERVER_ADDR
target_port = 1234

server_ip = '0.0.0.0'  
server_port = 1234

udp_socket.bind((server_ip, server_port))

message = "Hello, UDP Server!"

udp_socket.sendto(message.encode(), (target_host, target_port))

data, addr = udp_socket.recvfrom(1024)
print(data.decode())

udp_socket.close()