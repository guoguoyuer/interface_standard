from hit import *
import unittest

class AddEvent(unittest.TestCase):

    def setUp(self):
        url = DATA.get('base_url') + 'add_event/'
        method = Method.POST
        type = Type.URL_ENCODE
        self.client = Client(url=url, method=method, type=type)
        self.token = self.client.value('token')
        self.uid = self.client.value('uid')

    def tearDown(self):
        self.client.db_values("delete from api_event where title='慧测接口测试大会222'")

    def test_add_event01(self):
        '''登录接口主流程'''
        self.client.set_headers({'cookie': 'token=%s;uid=%s' % (self.token, self.uid)})
        self.client.set_data({'title': '慧测接口测试大会222', 'address': '汤立路220号院', 'time': '2019-01-01 10:00:00'})
        self.client.add_sign(token=self.token)
        self.client.send()
        self.client.check_jsonNode_equal('$.error_code', 0)
        self.client.check_db2('$.data.event_id', "select id from api_event where title='慧测接口测试大会222'")


