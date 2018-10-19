from hit import *
import unittest


class CreateAppointment(unittest.TestCase):
    def setUp(self):
        url = DATA.get('base_url') + '/api/v1/order/createAppointment'
        method = Method.POST
        type = Type.URL_ENCODE
        self.client = Client(url=url, method=method, type=type)
        self.token = self.client.value('token')
        self.appointment = self.client.appointment

    def test_createAppointment01(self):
        '''公务用餐预定流程'''
        self.client.set_data({"shop_id": "BA9FA2D804000000B5D6000000000000",
                              "token": self.token,
                              "accept_hall": "",
                              "room": "",
                              "buildLevel": "22",
                              "appointment_num": "3",
                              "appVersion": "127",
                              "invoice_id": "E66323265C000000E000000000155000",
                              "phoneBrand": "Meizu",
                              "deviceOs": "5.1",
                              "appointment": self.appointment,
                              "for_meal": "部门团建",
                              "appPort": "Android",
                              "customer_name": "陈",
                              "customer_gender": "1",
                              "seat_id": "4",
                              "phoneModel": "MX5",
                              "customer_phone": "18600274969",
                              "order_type": "0"  # 公务用餐
                              })
        self.client.send()
        logger.info(self.client.text)
        self.client.check_status_code(200)
        self.client.check_jsonNode_equal('$..msg', '操作成功')

    def test_createAppointment02(self):
        '''工作餐预定流程'''
        self.client.set_data({"shop_id": "BA9FA2D804000000B5D6000000000000",
                              "token": self.token,
                              "accept_hall": "",
                              "room": "",
                              "buildLevel": "22",
                              "appointment_num": "3",
                              "appVersion": "127",
                              "invoice_id": "E66323265C000000E000000000155000",
                              "phoneBrand": "Meizu",
                              "deviceOs": "5.1",
                              "appointment": self.appointment,
                              "appPort": "Android",
                              "customer_name": "陈",
                              "customer_gender": "1",
                              "seat_id": "4",
                              "phoneModel": "MX5",
                              "customer_phone": "18600274969",
                              "order_type": "2"  # 工作餐
                              })
        self.client.send()
        self.client.check_status_code(200)
        self.client.check_jsonNode_equal('$..msg', '操作成功')

    def test_createAppointment03(self):
        '''私人用餐预定流程'''
        self.client.set_data({"shop_id": "BA9FA2D804000000B5D6000000000000",
                              "token": self.token,
                              "accept_hall": "",
                              "room": "",
                              "buildLevel": "22",
                              "appointment_num": "3",
                              "appVersion": "127",
                              "invoice_id": "E66323265C000000E000000000155000",
                              "phoneBrand": "Meizu",
                              "deviceOs": "5.1",
                              "appointment": self.appointment,
                              "appPort": "Android",
                              "customer_name": "陈",
                              "customer_gender": "1",
                              "seat_id": "4",
                              "phoneModel": "MX5",
                              "customer_phone": "18600274969",
                              "order_type": "1"  # 私人用餐
                              })
        self.client.send()
        self.client.check_status_code(200)
        self.client.check_jsonNode_equal('$..msg', '操作成功')
