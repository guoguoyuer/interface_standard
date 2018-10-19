from hit import *
import unittest


class UpdateOrderStatus(unittest.TestCase):
    def setUp(self):
        url = DATA.get('base_url') + '/api/v1/order/updateOrderStatus'
        method = Method.POST
        type = Type.URL_ENCODE
        self.client = Client(url=url, method=method, type=type)
        self.order_id = self.client.value('order_id')
        self.token = self.client.value('mtoken')

    def test_updateOrderStatus01(self):
        '''新订单拒绝'''
        self.client.set_data({"appVersion": "35",
                              "status": "6",  # 拒绝
                              "room_name": "",
                              "token": self.token,
                              "remark": "休息时间不接单",
                              "phoneBrand": "Meizu",
                              "deviceOs": "5.1",
                              "appPort": "Android",
                              "order_id": self.order_id,
                              "room_id": "",
                              "before_status": "0",
                              "phoneModel": "MX5",
                              "buildLevel": "22",
                              })
        self.client.send()
        self.client.check_status_code(200)
        self.client.check_jsonNode_equal('$..msg', '操作成功')
