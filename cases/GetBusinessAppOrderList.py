from hit import *
import unittest


class GetBusinessAppOrderList(unittest.TestCase):
    def setUp(self):
        url = DATA.get('base_url') + '/api/v1/order/getBusinessAppOrderList'
        method = Method.GET
        self.client = Client(url=url, method=method)
        self.token = self.client.value('mtoken')

    def test_getBusinessAppOrderList01(self):
        '''订单接口流程（新订单）'''
        self.client.set_data({"shop_id": "BA9FA2D804000000B5D6000000000000",
                              "appVersion": "35",
                              "token": self.token,
                              "phoneBrand": "Meizu",
                              "deviceOs": "5.1",
                              "appPort": "Android",
                              "page_size": "20",
                              "phoneModel": "MX5",
                              "buildLevel": "22",
                              "page_num": "1",
                              "type": "1"  # 1-新订单，2-待结账，3-已完成
                              })
        self.client.send()
        self.client.check_status_code(200)
        self.client.check_jsonNode_equal('$..msg', '操作成功')
        self.client.transmit('order_id', '$..id')

    def test_getBusinessAppOrderList02(self):
        '''订单接口流程（待结账）'''
        self.client.set_data({"shop_id": "BA9FA2D804000000B5D6000000000000",
                              "appVersion": "35",
                              "token": self.token,
                              "phoneBrand": "Meizu",
                              "deviceOs": "5.1",
                              "appPort": "Android",
                              "page_size": "20",
                              "phoneModel": "MX5",
                              "buildLevel": "22",
                              "page_num": "1",
                              "type": "2"  # 1-新订单，2-待结账，3-已完成
                              })
        self.client.send()
        self.client.check_status_code(200)
        self.client.check_jsonNode_equal('$..msg', '操作成功')
        self.client.transmit('order_id', '$..id')

    def test_getBusinessAppOrderList03(self):
        '''订单接口流程（已完成）'''
        self.client.set_data({"shop_id": "BA9FA2D804000000B5D6000000000000",
                              "appVersion": "35",
                              "token": self.token,
                              "phoneBrand": "Meizu",
                              "deviceOs": "5.1",
                              "appPort": "Android",
                              "page_size": "20",
                              "phoneModel": "MX5",
                              "buildLevel": "22",
                              "page_num": "1",
                              "type": "3"  # 1-新订单，2-待结账，3-已完成
                              })
        self.client.send()
        self.client.check_status_code(200)
        self.client.check_jsonNode_equal('$..msg', '操作成功')
        self.client.transmit('order_id', '$..id')
