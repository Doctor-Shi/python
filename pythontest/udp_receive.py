import socket

PORT = 6666
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("172.20.8.80", PORT)
send_address = ("172.20.8.120", 6661)
server_socket.bind(address)
while True:
    receive_data, client_address = server_socket.recvfrom(1024)
    print("接收到了客户端 %s 传来的数据 : %s", (client_address, receive_data))



