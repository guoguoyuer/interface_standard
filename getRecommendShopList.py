from hit import *


class getRecommendShopList():
    def getRecommendShopList04(self):
        '''查询推荐餐厅列表'''
        url = DATA.get('https_base_url') + '/api/v1/sys/updateSysParams'
        method = Method.POST
        type = Type.JSON
        self.client = Client(url=url, method=method, type=type)
        self.client.set_data(
            {"token": "SEhULVNFQ1RFVDoxNTM4MjA0MDQ0OjEw", "param_value": "", "value_type": "selected", "id": "7"})
        self.client.send()
        print(self.client.text)
        print(self.client.status_code)
        # data=self.client.db_values("select current_amount from user_account where user_id='D8A11B4F1C0000008000000000155000'")[0][0]
        # self.client.db_transmit('current_amount',"select current_amount from user_account where user_id='D8A11B4F1C0000008000000000155000'")
        # self.client.db_transmit('ErrorShopAward',
        #                         "select param_value from sys_params where param_key='ERROR_SHOP_AWARD'")
        # print(self.client.value('ErrorShopAward'))


if __name__ == '__main__':
    a = getRecommendShopList()
    a.getRecommendShopList04()
