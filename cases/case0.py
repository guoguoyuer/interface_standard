from hit import *

#1无参数的get
# client1 = Client(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince', method=Method.GET)
# client1.send()
# print(client1.text)

#2有参数的get
# client2 = Client(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString', method=Method.GET)
# client2.set_params({'theRegionCode': '3113'})
# client2.send()
# print(client2.text)

#3无参数的post
# client3 = Client(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince', method=Method.POST)
# client3.send()
# print(client3.text)

#4有正文体的post --urlencode
# client4 = Client(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString',
#                  method=Method.POST,
#                  type=Type.URL_ENCODE)
# client4.set_data({'theRegionCode': '3113'})
# client4.send()
# print(client4.text)

#5有正文体的post --form
# client5 = Client(url=' ',
#                  method=Method.POST,
#                  type=Type.FORM)
# client5.set_data({'username': 'tianhaha', 'password': '123456', 'email': 'huice@163.com'})
# client5.send()
# print(client5.text)

#6有正文体的post --form带文件
# client6 = Client(url='http://139.199.132.220:9000/event/index/uploadFile/',
#                  method=Method.POST,
#                  type=Type.FILE)
# client6.set_data({'myfile': open('./1.txt', 'rb')})
# client6.send()
# print(client6.text)

#7有正文体的post --json
# client7 = Client(url='http://139.199.132.220:9000/event/weather/getWeather/',
#                  method=Method.POST,
#                  type=Type.JSON)
# client7.set_data({'theCityCode': 1})
# client7.send()
# print(client7.text)
# print(client7.res_cookies)
# print(client7.res_headers)
# print(client7.res_time)

#8有正文体的post --xml
# client8 = Client(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx',
#                  method=Method.POST,
#                  type=Type.XML)
# xml = '''<?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <getSupportCityString xmlns="http://WebXml.com.cn/">
#       <theRegionCode>3113</theRegionCode>
#     </getSupportCityString>
#   </soap:Body>
# </soap:Envelope>'''
# client8.set_data({'xml': xml})
# client8.send()
# print(client8.text)

#9 post业务接口
# url = 'http://139.199.132.220:9000/event/api/add_event/'
# headers = {'cookie': 'token=75ff30521dd7bafb48e07cf7e0a0b564dd8896a4;uid=1'}
# data = {'title': '慧测001', 'address': '汤立路220号院', 'time': '2019-01-01 10:00:00',
#         'sign': '5af178cf6ab9f9176fe2b75f645e939b'}
# client9 = Client(url=url, method=Method.POST, type=Type.URL_ENCODE)
# client9.set_headers(headers)
# client9.set_data(data)
# client9.send()
# client9.check_status_code(200)


