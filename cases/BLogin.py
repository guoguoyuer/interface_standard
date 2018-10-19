from hit import *
import unittest


class BLogin(unittest.TestCase):
    def setUp(self):
        url = DATA.get('base_url') + '/api/v1/passport/login'
        method = Method.POST
        type = Type.URL_ENCODE
        self.client = Client(url=url, method=method, type=type)

    def test_login01(self):
        '''登录接口正向流程'''
        self.client.set_data({"appVersion": "127",
                              "phoneBrand": "Meizu",
                              "deviceOs": "5.1",
                              "appPort": "Android",
                              "phone": "18600274969",
                              "port": "8",
                              "phoneModel": "MX5",
                              "buildLevel": "22",
                              "code": "161891"})
        self.client.send()
        self.client.check_status_code()
        self.client.check_jsonNode_equal('$..msg', '操作成功')
        # self.client.check_db2('$.uid', "select id from auth_user where username='huice'")
        # self.client.check_db2('$.token', "select authtoken_token.key from auth_user, authtoken_token "
        #                                  "where auth_user.username='huice' and authtoken_token.user_id=auth_user.id")
        self.client.transmit('token', '$..token')

    def test_login02(self):
        '''登录接口反向流程：手机号为空'''
        self.client.set_data({"appVersion": "127",
                              "phoneBrand": "Meizu",
                              "deviceOs": "5.1",
                              "appPort": "Android",
                              "phone": "",
                              "port": "8",
                              "phoneModel": "MX5",
                              "buildLevel": "22",
                              "code": "161891"})
        self.client.send()
        self.client.check_jsonNode_equal('$..code', 402)
        self.client.check_jsonNode_equal('$..msg', '请填写正确的手机号码')


    def test_login03(self):
        '''登录接口返向流程：验证码为空'''
        self.client.set_data({"appVersion": "127",
                              "phoneBrand": "Meizu",
                              "deviceOs": "5.1",
                              "appPort": "Android",
                              "phone": "18600274969",
                              "port": "8",
                              "phoneModel": "MX5",
                              "buildLevel": "22",
                              "code": ""})
        self.client.send()
        self.client.check_jsonNode_equal('$..code', 400)
        self.client.check_jsonNode_equal('$..msg', '系统参数错误')

    def test_login04(self):
        '''登录接口返向流程：验证码错误'''
        self.client.set_data({"appVersion": "127",
                              "phoneBrand": "Meizu",
                              "deviceOs": "5.1",
                              "appPort": "Android",
                              "phone": "18600274969",
                              "port": "8",
                              "phoneModel": "MX5",
                              "buildLevel": "22",
                              "code": "111111"})
        self.client.send()
        self.client.check_jsonNode_equal('$..code', 412)
        self.client.check_jsonNode_equal('$..msg', '请正确填写验证码')
