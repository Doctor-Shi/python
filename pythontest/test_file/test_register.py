import socket
import time
import uuid

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("192.172.0.103", 5060)  # 接收方 服务器的ip地址和端口号
client_address = ("192.172.0.79", 18820)
client_socket.bind(client_address)


def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4())  # Convert UUID format to a Python string.
    random = random.upper()  # Make all characters uppercase.
    random = random.replace("-", "")  # Remove the UUID '-'.
    return random[0:string_length]  # Return the random string


ssi = "16566072"
CAllid = my_random_string(8)
reg_sip = "R p:"+ssi+"\r\n" \
          "i:"+CAllid+"\r\n" \
          "f:<p:"+ssi+">;g=lysK\r\n" \
          "t:-\r\n" \
          "Q:492 R\r\n" \
          "v:r119.pdt.cn;b=5%q\r\n" \
          "m:<s:r119.pdt.cn;m=192.172.0.79:18820>\r\n" \
          "H:70\r\n" \
          "ua:46 ACTEC-PDT-RCU-1.5.0.0\r\n" \
          "c:a/m\r\n" \
          "l:44\r\n" \
          "\r\n" \
          "<attachgroup><AG>16550841</AG></attachgroup>"

while True:
    client_socket.sendto(reg_sip.encode(), server_address)
    result = client_socket.recv(1024)
    print(result)
    time.sleep(10)
client_socket.close()

