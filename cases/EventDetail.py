from hit import *
import unittest

class EventDetail(unittest.TestCase):

    def setUp(self):
        url = DATA.get('base_url') + 'get_eventdetail/'
        method = Method.GET
        self.client = Client(url=url, method=method)
        self.token = self.client.value('token')
        self.uid = self.client.value('uid')
        self.eid = self.client.db_values('select id from api_event')[0][0]

    def test_get_eventdetail01(self):
        self.client.set_headers({'cookie': 'token=%s;uid=%s' % (self.token, self.uid)})
        self.client.set_data({'id': self.eid})
        self.client.add_sign(token=self.token)
        self.client.send()
        self.client.check_jsonNode_equal('$.error_code', 0)
        self.client.check_jsonNode_equal('$.event_detail.id', str(self.eid))