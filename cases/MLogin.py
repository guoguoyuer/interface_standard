from hit import *
import unittest


class MLogin(unittest.TestCase):
    def setUp(self):
        url = DATA.get('base_url') + '/api/v1/user/loginByPwd'
        method = Method.POST
        type = Type.URL_ENCODE
        self.client = Client(url=url, method=method, type=type)

    def test_login01(self):
        '''登录接口流程'''
        self.client.set_data({"appVersion": "35",
                              "phoneBrand": "Meizu",
                              "deviceOs": "5.1",
                              "appPort": "Android",
                              "phone": "13811249171",
                              "pwd": "a7ba6215bc914a3f6dc989ab0aa17a08",
                              "phoneModel": "MX5",
                              "buildLevel": "22"
                              })
        self.client.send()
        self.client.check_status_code(200)
        self.client.check_jsonNode_equal('$..msg', '操作成功')
        # self.client.check_db2('$.uid', "select id from auth_user where username='huice'")
        # self.client.check_db2('$.token', "select authtoken_token.key from auth_user, authtoken_token "
        #                                  "where auth_user.username='huice' and authtoken_token.user_id=auth_user.id")
        self.client.transmit('mtoken', '$..token')
        # self.client.transmit('uid', '$.uid')
