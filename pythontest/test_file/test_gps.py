import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("192.172.0.120", 6000)  # 接收方 服务器的ip地址和端口号
# client_socket.bind(("", 18820))  # 参数是元组的形式
# msg = input("请输入要发送的内容：")  # 字符串类型， 通过msg.encode() 编码 转换为bytes类型
uri = 80520800
uri_cn = 'r82.zj.pdt.cn'
while True:

    GPS_MSG = "$GPGLL," + uri_cn + ",3010.958,N,12009.205,E,V,,,025737.804,,-61,B,15,, ,,,r82.zj.pdt.cn,3182,,,,,,,*70"
    print(GPS_MSG)
    client_socket.sendto(GPS_MSG.encode(), server_address)
    # uri += 1
    time.sleep(5)

