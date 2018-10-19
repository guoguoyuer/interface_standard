import requests
import hashlib
import unittest
import jsonpath
import util
import sys
import pymysql
import os
import datetime



# import logging
# import logging.config


class Method:
    POST = 'POST'
    GET = 'GET'


class Type:
    URL_ENCODE = 1
    FORM = 2
    JSON = 3
    XML = 4
    FILE = 5
    none = 9


class DATABASE:
    # re = util.read_config(sys.argv[0] + '/../config.xml', './/config/database/*')
    # xml驱动版本
    # re = util.read_config(os.path.dirname(__file__) + '/config.xml', './/config/database/*')
    # HOST = re.get('host')
    # USER = re.get('user')
    # PASSWORD = re.get('password')
    # NAME = re.get('db')

    # excel驱动版本
    re = util.read_config_excel(sys.argv[0] + '/../cases.xlsx', '数据库配置')
    data = re.get('数据库配置')
    if data:
        HOST = data[0].get('地址')
        USER = data[0].get('用户名')
        PASSWORD = data[0].get('密码')
        NAME = data[0].get('数据库')


# DATA = util.read_config(sys.argv[0] + '/../config.xml', './/config/data/*')
# xml驱动版本
# DATA = util.read_config(os.path.dirname(__file__) + '/config.xml', './/config/data/*')

# excel驱动版本
data = util.read_config_excel(sys.argv[0] + '/../cases.xlsx', '全局数据').get('全局数据')
DATA = {}
if data:
    for d in data:
        DATA[d.get('变量名')] = d.get('变量值')

logger = util.read_logconfig(os.path.dirname(__file__) + '\config\logging.conf')


# logger = util.logger


class Client(unittest.TestCase):
    VALAUES = {}

    def __init__(self, url, method, type=0):
        self.__url = url
        self.__method = method
        self.__headers = {}
        self.__type = type
        self.__data = {}
        self.__res = None
        self._type_equality_funcs = {}

    def add(func):
        def wrapper(self, first, second, msg=None):
            try:
                func(self, first, second, msg=None)
                logger.info('检查点成功。实际结果：[{first}]，预期结果：[{second}]'.format(first=first, second=second))
            except AssertionError as e:
                logger.error('检查点失败：{0}'.format(e))
                raise AssertionError()

        return wrapper

    def set_headers(self, headers):
        if isinstance(headers, dict):
            self.__headers = headers
        else:
            logger.debug('headers类型为字典')
            raise Exception('headers类型为字典')

    def set_data(self, data):
        if isinstance(data, dict):
            if self.__type == 1:
                self.__headers['Content-type'] = 'application/x-www-form-urlencoded'
            elif self.__type == 2 or self.__type == 5 or self.__type == 0 or self.__type == 9:
                pass
            elif self.__type == 3:
                self.__headers['Content-type'] = 'application/json'
            elif self.__type == 4:
                self.__headers['Content-type'] = 'text/xml'
            # elif self.__type == 0:
            #     raise Exception('未设置请求正文类型，无法传递正文内容')
            else:
                raise Exception('请求正文类型不存在')
                logger.debug('请求正文类型不存在')
            self.__data = data
        else:
            raise Exception('data类型为字典，如果为xml正文：{"xml": xml字符串}')
            logger.debug('data类型为字典，如果为xml正文：{"xml": xml字符串}')

    def send(self):
        logger.info('=========开始执行测试用例，接口：' + self.__url)
        if self.__method == 'GET':
            self.__res = requests.get(url=self.__url, params=self.__data, headers=self.__headers)
        elif self.__method == 'POST':
            if self.__type == 0:
                # self.__res = requests.post(url=self.__url, params=self.__data, headers=self.__headers)
                self.__res = requests.post(url=self.__url, headers=self.__headers)
            else:
                if self.__type == 1 or self.__type == 2:
                    self.__res = requests.post(url=self.__url, data=self.__data, headers=self.__headers)
                elif self.__type == 3:
                    self.__res = requests.post(url=self.__url, json=self.__data, headers=self.__headers)
                elif self.__type == 4:
                    xml_str = self.__data.get('xml')
                    if xml_str and isinstance(xml_str, str):
                        self.__res = requests.post(url=self.__url, data=xml_str, headers=self.__headers)
                    else:
                        raise Exception('xml正文的请求，请正确添加xml字符串')
                        logger.debug('xml正文的请求，请正确添加xml字符串')
                elif self.__type == 5:
                    self.__res = requests.post(url=self.__url, files=self.__data, headers=self.__headers)
        else:
            raise Exception('不支持的请求方法类型')
            logger.error('xml正文的请求，请正确添加xml字符串')

    def add_sign(self, token):
        list = []
        for k, v in self.__data.items():
            if k != 'username':
                list.append('%s=%s' % (k, v))
        list.sort()
        sign_str = "%spara=%s" % (token, '&'.join(list))
        md5 = hashlib.md5()
        md5.update(sign_str.encode(encoding="utf-8"))
        sign = md5.hexdigest()
        self.__data['sign'] = sign

    @property
    def url(self):
        return self.__url

    @property
    def method(self):
        return self.__method

    @property
    def type(self):
        return self.__type

    @property
    def text(self):
        if any(self.__res):
            logger.debug('响应为：{0}'.format(self.__res.text))
            return self.__res.text
        else:
            logger.error('响应为空，无法获取响应body')
            return None

    @property
    def status_code(self):
        if any(self.__res):
            return self.__res.status_code
        else:
            logger.error('响应为空，无法获取响应status_code')
            return None

    @property
    def res_cookies(self):
        if any(self.__res):
            return requests.utils.dict_from_cookiejar(self.__res.cookies)
        else:
            logger.error('响应为空，无法获取响应cookies')
            return None

    @property
    def res_headers(self):
        if any(self.__res):
            return self.__res.headers
        else:
            logger.error('响应为空，无法获取响应headers')
            return None

    @property
    def res_time(self):
        if any(self.__res):
            return round(self.__res.elapsed.total_seconds() * 1000)
        else:
            logger.error('响应为空，无法获取响应时间')
            return None

    @property
    #第二天 15:00:00
    def appointment_tmr(self):
        appt = str((datetime.datetime.now() + datetime.timedelta(days=1)).replace(hour=15, minute=0, second=0,
                                                                                  microsecond=0).timestamp() * 1000).split(
            '.')[0]
        return appt

    @property
    #当天 23:30:00
    def appointment_today(self):
        appt = str((datetime.datetime.now() + datetime.timedelta(days=0)).replace(hour=23, minute=30, second=0,
                                                                                  microsecond=0).timestamp() * 1000).split(
            '.')[0]
        return appt

    def res_to_json(self):
        if any(self.__res):
            try:
                return self.__res.json()
            except:
                logger.error('响应不为空，反序列化失败')
                return None
        else:
            logger.error('响应为空，反序列化失败')
            return None

    def check_status_code(self, status=200):
        if any(self.__res):
            self.assertEqual(self.__res.status_code, status,
                             '响应状态码错误。实际结果：[{first}]，预期结果：[{second}]'.format(first=str(self.__res.status_code),
                                                                             second=status))
            logger.info('响应状态码检查成功。实际结果：[{first}]，预期结果：[{second}]'.format(first=str(self.__res.status_code),
                                                                          second=status))

        else:
            self.assertTrue(False, '无法获取响应状态码')
            logger.info('无法获取响应状态码')

    @add
    def check_equal(self, first, second, msg=None):
        self.assertEqual(first, second, msg=msg)

    @add
    def check_not_equal(self, first, second, msg=None):
        self.assertNotEqual(first, second, msg=msg)

    def json_value(self, path):
        if any(self.__res):
            object = jsonpath.jsonpath(self.res_to_json(), path)
            if object:
                return object[0]
        return None

    def json_values(self, path):
        if any(self.__res):
            object = jsonpath.jsonpath(self.res_to_json(), path)
            if object:
                return object
        return None

    def check_jsonNode_equal(self, path, exp, msg=None):
        node = self.json_value(path)
        try:
            self.assertEqual(node, exp, msg)
            logger.info('检查点成功。实际结果：[{first}]，预期结果：[{second}]'.format(first=node, second=exp))
        except AssertionError as e:
            logger.error('检查点失败：{0}'.format(e))
            raise AssertionError()

    def transmit(self, name, path):
        node = self.json_value(path)
        if node:
            Client.VALAUES[name] = node
        else:
            logger.info('未获取到要传递的值:' + path)
            raise Exception('未获取到要传递的值:' + path)

    def db_transmit(self, name, sql):
        node = self.db_values(sql)[0][0]
        if node:
            Client.VALAUES[name] = node
        else:
            logger.info('数据库中未获取到要传递的值:' + sql)
            raise Exception('数据库中未获取到要传递的值:' + sql)

    def value(self, name):
        v = Client.VALAUES.get(name)
        if v:
            return v
        else:
            raise Exception('要获取的变量不存在:' + name)
            logger.info('要获取的变量不存在:' + name)

    def db_values(self, sql):
        if DATABASE.HOST and DATABASE.USER and DATABASE.PASSWORD and DATABASE.NAME:
            db = None
            try:
                db = pymysql.connect(host=DATABASE.HOST, user=DATABASE.USER, password=DATABASE.PASSWORD,
                                     db=DATABASE.NAME)
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
        else:
            raise Exception('数据库链接参数错误')
            logger.info('数据库连接参数错误')

    def check_db1(self, exp, sql):
        data = self.db_values(sql)
        if data:
            self.check_equal(str(exp), str(data[0][0]))
        else:
            self.assertFalse(True, '数据库取值无效：' + sql)

    def check_db2(self, path, sql):
        data = self.db_values(sql)
        exp = str(self.json_value(path))
        if data:
            if exp:
                self.check_equal(exp, str(data[0][0]))
            else:
                self.assertFalse(True, 'json取值无效：' + path)
                logger.error('json取值无效：' + path)
        else:
            self.assertFalse(True, '数据库取值无效：' + sql)
            logger.error('数据库取值无效：' + sql)
