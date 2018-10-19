from hit import *


class getRecommendShopList():
    def setUp(self):
        url = DATA.get('base_url') + '/api/v1/recommendShop/getRecommendShopList'
        method = Method.GET
        type = Type.none
        self.client = Client(url=url, method=method, type=type)

    def test_getRecommendShopList01(self):
        '''查询推荐餐厅列表'''
        self.client.set_data(
            {"token": "SEhULVNFQ1RFVDoxNTM4MDMxODIyOjEw", "page_num": "12", "page_size": "20", "shop_name": "",
             "star": "", "user_name": "", "user_phone": "", "hendle": "", "type": "0"})
        self.client.send()
        self.client.check_status_code(200)
        self.client.check_jsonNode_equal('$..msg', '操作成功')

if __name__ == '__main__':
    a = getRecommendShopList()
    a.test_getRecommendShopList01()
