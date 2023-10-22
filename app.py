import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = '0.0.0.0'  
server_port = 1234

udp_socket.bind((server_ip, server_port))

print(f"Listening on {server_ip}:{server_port}")

while True:
    data, addr = udp_socket.recvfrom(1024)

    message = data.decode()

    print(f"Received from {addr}: {message}")