import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))

server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

message, address = server_socket.recvfrom(1024)
print(message.decode("utf-8"))
print(address)