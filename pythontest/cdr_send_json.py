import httplib2
import json


def test_http_post():

    url_str = 'http://172.20.8.129:7200'
    # headers = {'Content-Type': 'application/json-rpc'}

    # 配置订阅号码
    test_dat = {'timestamp': 1524797874000, 'object': 'r151.pdt.cn$D002$', 'level': 0, 'type':	0, 'code': 15,
                'description': '$X101001$', 'pfix': 801, 'sys_domain': 'm2.zj.pdt.cn', 'ne': ''}

    h = httplib2.Http('.cache')
    content = h.request(url_str, 'POST', json.dumps(test_dat))


test_http_post()
