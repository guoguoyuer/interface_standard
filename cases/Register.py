import unittest
from hit import *

class Register(unittest.TestCase):

    def setUp(self):
        url = DATA.get('base_url') + 'register/'
        method = Method.POST
        type = Type.URL_ENCODE
        self.client = Client(url=url, method=method, type=type)

    def test_register01(self):
        '''登录接口主流程'''
        self.client.set_data({'username': 'huice', 'password': 'MTIzaHVpY2VodWljZSFAIw=='})
        self.client.send()
        self.client.check_status_code(200)
        self.client.check_jsonNode_equal('$.error_code', 0)
        self.client.check_db2('$.uid', "select id from auth_user where username='huice'")
        self.client.check_db2('$.token', "select authtoken_token.key from auth_user, authtoken_token "
                                         "where auth_user.username='huice' and authtoken_token.user_id=auth_user.id")
        self.client.transmit('token', '$.token')
        self.client.transmit('uid', '$.uid')

    def test_register02(self):
        '''登录接口用户名密码为空'''
        self.client.set_data({'username': 'huice', 'password': ''})
        self.client.send()
        self.client.check_status_code(200)
        self.client.check_jsonNode_equal('$.error_code', 10001)
        # text = self.client.res_to_json()
        # self.client.check_equal(text['error_code'], 10001)

