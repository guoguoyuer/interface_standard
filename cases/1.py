import requests
from io import BytesIO
# --coding=utf8--

import sys
import pymysql


def init_db():
    try:
        conn = pymysql.connect(host=conf.get('Database', 'host'),
                               user=conf.get('Database', 'user'),
                               passwd=conf.get('Database', 'passwd'),
                               db=conf.get('Database', 'db'),
                               charset='utf8')
        return conn
    except:
        print
        "Error:数据库连接错误"
        return None


# def select_demo(conn, sql):
#     try:
#         cursor = conn.cursor()
#         cursor.execute(sql)
#         return cursor.fetchall()
#     except:
#         print
#         "Error:数据库连接错误"
#         return None

def db_values(sql):
    try:
        db = pymysql.connect(host='47.93.38.221', user='hhtdev', password='hhtdev',
                             db='hht_cloud')
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        return cursor.fetchall()
    except Exception as e:
        raise Exception('数据库操作失败')
        logger.error('数据库操作失败:{0}'.format(e))
    finally:
        if db:
            db.close()

if __name__ == '__main__':
    sql = "select month_amount from dept_limit where dept_id='E9079F5190000000D800000000155000' and `month`=month(CURRENT_DATE)"
    data = db_values(sql)[0][0]
    print(data)
    print(type(data))
    print(2000+data)


# url = 'http://139.199.132.220:9000/event/index/uploadFile/'
# # data = {'file': open('D:/demo.html', 'rb')}
# fm = open('D:/demo.html', 'rb')
# print(fm)
# res = requests.post(url=url, files={'file': fm})
# print(res.text)

# url = 'http://pythontab.com/postTest'
# files = {'file': open('D:/demo.html', 'rb')}
# r = requests.post(url, files=files)
# print(r.text)



# >>> url = 'http://pythontab.com/postTest'
#
# >>> files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
#
# >>> r = requests.post(url, files=files)

# host = 'http://test-api-c2b.honghuotai.com'
# url = '/api/v1/user/loginByPwd'
# data = {"appVersion": "35", "phoneBrand": "Meizu", "deviceOs": "5.1", "appPort": "Android", "phone": "13811249171",
#         "pwd": "a7ba6215bc914a3f6dc989ab0aa17a08", "phoneModel": "MX5", "buildLevel": "22"}
#
# headers = {"Content-Type": "application/x-www-form-urlencoded"}
# res = requests.post(url=host + url, data=data, headers=headers)
# print(res.text)

# host = 'http://test-api-c2b.honghuotai.com'
# url = '/api/v1/order/getBusinessAppOrderList'
# data = {"shop_id": "BA9FA2D804000000B5D6000000000000", "appVersion": "35", "token": "SEhULVNFQ1RFVDoxNTM4MDEyMDcyOkJBNzA2RTFBQjAwMDAwMDBCMTQ4MDAwMDAwMDAwMDAw",
#         "phoneBrand": "Meizu", "deviceOs": "5.1", "appPort": "Android", "page_size": "20", "phoneModel": "MX5",
#         "buildLevel": "22", "page_num": "1", "type": "1"}
# headers = {"Content-Type": "application/x-www-form-urlencoded"}
# res = requests.post(url=host + url, data=data, headers=headers)
# print(res)
# print(res.status_code)
# print(res.text)
# print(type(res.text))
# print(res.json())
# print(type(res.json()))
