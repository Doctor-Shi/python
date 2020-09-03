def test_http_post():
    import httplib2
    import json
    urlstr = 'http://172.20.8.129:8081/index.json'
    headers = {'Content-Type': 'application/json-rpc'}

    # 配置订阅号码
    data_add = {'id': 1, 'jsonrpc': "2.0", 'method': 'app_request_add_other_user_onoff',
                'params': {'auth': '-', 'tag': '557e90880042020', 'ssi': '80120271,80166203'}}
    # 删除配置订阅的号码
    data_remove = {"id": 1, "jsonrpc": "2.0", "method": "app_request_remove_other_user_onoff",
                   "params": {"auth": "-", "tag": "557e90880042020", "ssi": "80120271,80166203"}}
    # 批量配置订阅号码

    batch_data_add = {'id': 1, 'jsonrpc': "2.0", 'method': 'app_request_batch_add_other_user_onoff',
                'params': {'auth': '-', 'tag': '557e90880042020', 'ssi-min': '80120201', 'ssi-max': '80120204'}}
    # 批量删除配置订阅的号码
    batch_data_remove = {"id": 1, "jsonrpc": "2.0", "method": "app_request_batch_remove_other_user_onoff",
                   "params": {"auth": "-", "tag": "557e90880042020", 'ssi-min': '80120201', 'ssi-max': '80166203'}}
    # 查询配置过订阅的号码
    data_load = {"id": 1, "jsonrpc": "2.0", "method": "app_request_query_other_user_onoff",
                 "params": {"auth": "-", "tag": "564be2b4c4d5"}}
    # 单独查询配置过订阅的号码
    single_data_load = {"id": 1, "jsonrpc": "2.0", "method": "app_request_query_single_other_user_onoff",
                 "params": {"auth": "-", "tag": "564be2b24c4d5","ssi": "80166203"}}
    # 查询配置过订阅中的在线状态的号码
    data_query = {"id": 1, "jsonrpc": "2.0", "method": "app_request_registered_radio_info",
                  "params": {"auth": "-", "rcu_uri": "r14@pdt.cn", "tag": "557E90B800042020"}}

    test_dat = {"id": 1, "jsonrpc": "2.0", "method": "app_request_sxu_interconnected_attributes",
                 "params": {"auth": "-", "sxu_uri": "sxu.pdt.cn", "tag": "564be2b4c4d5"}}

    test_beijing = {" timestamp ":"1234565878"," object ":"m1.zj.pdt.cn"," level ":"0" ," type ":"1","code":21, " description ":"101001"," ne ":"0"}
    h = httplib2.Http('.cache')

    response, content = h.request(urlstr, 'POST', json.dumps(single_data_load), headers)

    print(content.decode('utf-8'))

test_http_post()

