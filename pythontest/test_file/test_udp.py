import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("172.20.8.129", 5060)  # 接收方 服务器的ip地址和端口号
client_address = ("172.20.8.80", 18820)
client_socket.bind(client_address)
# client_socket.bind(("", 18820))  # 参数是元组的形式
# msg = input("请输入要发送的内容：")  # 字符串类型， 通过msg.encode() 编码 转换为bytes类型
GPS_MSG = "$GPGLL,80150200,3010.958,N,12009.205,E,A,,,025737.804,,-61,B,15,,80150903,,,r82.zj.pdt.cn,3182,,,,,,,*70"
reg_sip = "R p:16598810\r\n" \
          "i:vhaFY6Q1\r\n" \
          "f:<p:16598810>;g=lysK\r\n" \
          "t:-\r\n" \
          "Q:492 R\r\n" \
          "v:r69.zj.pdt.cn;b=5%q\r\n" \
          "m:<s:r69.zj.pdt.cn;m=172.20.8.80:18820>\r\n" \
          "H:70\r\n" \
          "ua:46 ACTEC-PDT-RCU-1.5.0.0\r\n" \
          "c:a/m\r\n" \
          "l:44\r\n" \
          "\r\n" \
          "<attachgroup><AG>16550842</AG></attachgroup>"
text_msg = "M p:16566047\r\n" \
           "i:Y/1/~+P]\r\n" \
           "f:<p:16566041>;g=xnXV\r\n" \
           "t:-\r\n" \
           "Q:651 M\r\n" \
           "v:r82.zj.pdt.cn;b=vK_E\r\n" \
           "m:<s:r82.zj.pdt.cn;m=192.168.88.9:18820>\r\n" \
           "H:70\r\n" \
           "ua:46 ACTEC-PDT-RCU-1.5.0.0\r\n" \
           "c:t/p;s=GB2312\r\n" \
           "l:10\r\n" \
           "\r\n" \
           "短信测试！"

while True:
    client_socket.sendto(reg_sip.encode(), server_address)
    result = client_socket.recv(1024)
    print(result)
    time.sleep(10)
client_socket.close()
