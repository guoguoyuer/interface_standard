import requests

class Client:

    def __init__(self, url, method, type=0):
        self.url = url
        self.method = method
        self.type = type
        self.headers = {}
        self.data = {}
        self.res = None

    @property
    def status_code(self):
        return self.res.status_code

    @property
    def text(self):
        return self.res.text

    @property
    def json(self):
        return self.res.json()

    @property
    def tiems(self):
        return int(round(self.res.elapsed.total_seconds() * 1000))

    def set_header(self, key, value):
        self.headers[key] = value

    def set_data(self, dic):
        if isinstance(dic, dict):
            self.data = dic
        else:
            raise Exception('请求参数请以字典格式传递')

    def send(self):
        if self.method == 'GET':
            self.res = requests.get(url=self.url, headers=self.headers, params=self.data)
        elif self.method == 'POST':
            if self.type == 1:
                self.res = requests.post(url=self.url, headers=self.headers, data=self.data)
            elif self.type == 5:
                self.res = requests.post(url=self.url, headers=self.headers, files=self.data)
            elif self.type == 2:
                self.set_header('Content-Type', 'application/x-www-form-urlencoded')
                self.res = requests.post(url=self.url, headers=self.headers, data=self.data)
            elif self.type == 3:
                self.set_header('Content-Type', 'text/xml')
                xml = self.data.get('xml')
                if xml:
                    self.res = requests.post(url=self.url, headers=self.headers, data=xml)
                else:
                    raise Exception('xml正文，入参格式：{"xml": "xxx"}')
            elif self.type == 4:
                self.set_header('Content-Type', 'application/json')
                self.res = requests.post(url=self.url, headers=self.headers, json=self.data)
            elif self.type == 0:
                self.res = requests.post(url=self.url, headers=self.headers)
            else:
                raise Exception('正文格式不自持')
        else:
            raise Exception('请求的方法类型不支持')

class Method:
    GET = 'GET'
    POST = 'POST'

class Type:
    FORM = 1
    URL_ENCODE = 2
    XML = 3
    JSON = 4
    FILE = 5

client = Client(url='http://139.199.132.220:9000/event/api/register/', method=Method.POST, type=Type.URL_ENCODE)
client.set_data({'username': 'huice', 'password': 'MTIzaHVpY2VodWljZSFAIw=='})
client.send()
print(client.status_code)
print(client.tiems)
print(client.json)

