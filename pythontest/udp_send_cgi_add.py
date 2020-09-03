import socket
import time


PORT = 6666
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("172.20.8.80", PORT)
send_address = ("172.20.8.120", 6661)
#server_socket.bind(address)

msg = b'\x01\x00\x00\x0016566110\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00(\xbbk\\)'


while True:
    print(msg)
    server_socket.send(msg, address)




