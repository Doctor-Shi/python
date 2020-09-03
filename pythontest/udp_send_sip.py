def send_sip():
    import socket
    import json
    addr = ("172.20.8.129", 7200)
    # 创建客户端UDP套接字

    test_dat = {'timestamp': 1524797874000, 'object': 'r151.pdt.cn$D002$', 'level': 0, 'type': 0, 'code': 15,
                'description': '$X101001$', 'pfix': 801, 'sys_domain': 'm2.zj.pdt.cn', 'ne': ''}


    data  = json.dumps(test_dat)

    udpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    request_uri ={'timestamp': 1524797874000, 'object': 'r151.pdt.cn$D002$', 'level': 0, 'type': 0, 'code': 15,
                'description': '$X101001$', 'pfix': 801, 'sys_domain': 'm2.zj.pdt.cn', 'ne': ''}
    #strr = request_uri.encode('utf-8')
    str = "11111111111"
    strr = str.encode('utf-8')
    # 向服务器端发送数据
    udpClient.sendto(data.encode(), ("172.20.8.129", 6001))

    udpClient.close()

send_sip()
