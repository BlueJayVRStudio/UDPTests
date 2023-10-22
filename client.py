import os
import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVER_ADDR = os.getenv("SERVER_ADDR")
target_host = SERVER_ADDR
target_port = 1234

message = "Hello, UDP Server!"

udp_socket.sendto(message.encode(), (target_host, target_port))

udp_socket.close()