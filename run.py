import unittest
import HTMLTestReportCN
import time
import shutil
import sys
import util
import re
from hit import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


def get(dic, name):
    source = dic.get(name)
    if source == None or source == '':
        return None
    else:
        variable_regexp = r"\$([\w_]+)"
        result = re.findall(variable_regexp, source)
        if len(result) > 0:
            value = DATA.get(result[0])
            if value:
                source = source.replace('$' + result[0], value)
            else:
                return None
        return source


def send_email(report_path):
    """
        to_list:发给谁
        sub:主题
        content:内容
        send_mail("aaa@126.com","sub","content")
        """

    mail_host = "smtp.qq.com"
    mail_port = 465
    to_list = ['270358772@qq.com']
    mail_user = '270358772@qq.com'
    mail_pass = 'lfhlayentuedbjih'

    with open(report_path, 'rb') as file:
        mail_body = file.read()
        me = "270358772@qq.com"
        text = MIMEText(mail_body, 'html', 'utf-8')
        msg = MIMEMultipart()
        msg.attach(text)

    msg['Subject'] = '红火台餐饮APP自动化测试报告'
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    try:
        s = smtplib.SMTP_SSL(mail_host, mail_port)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        ("邮件发送成功", to_list)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    # xml加载用例模式下
    # suite = unittest.defaultTestLoader.discover(start_dir=sys.argv[0] + '\\..', pattern='case*.py')
    # suite = unittest.TestSuite()
    # cases = util.read_runconfig(sys.argv[0] + '/../config.xml')
    # for case in cases:
    #     p_name = case.split('-')[0]
    #     c_name = case.split('-')[1]
    #     # p = importlib.import_module(package='cases.' + p_name, name=p_name)
    #     FUNC_TEMPLATE1 = 'from cases.{package} import {classes}'
    #     FUNC_TEMPLATE2 = 'suite.addTest({case}("test_{method}"))'
    #     exec(FUNC_TEMPLATE1.format(package=p_name, classes=p_name))
    #     exec(FUNC_TEMPLATE2.format(case=p_name, method=c_name))
    #
    # title = '%s.html' % time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    # fp = open(sys.argv[0] + '\\..\\report\\' + title, 'wb')
    # HTMLTestReportCN.HTMLTestRunner(stream=fp, title='接口测试报告',tester='guojl').run(suite)
    # fp.close()
    # shutil.copyfile(sys.argv[0] + '\\..\\report\\' + title, sys.argv[0] + '\\..\\report\\report.html')

    # excel加载用例模式下
    cases = util.read_config_excel(sys.argv[0] + '/../cases.xlsx', '用例').get('用例')
    if cases:
        suite = unittest.TestSuite()
        for case in cases:
            id = get(case, '用例编号')
            des = get(case, '用例描述')
            url = get(case, '地址')
            method = get(case, '方法类型')
            type = get(case, '参数类型')
            headers = get(case, '请求头')
            data = get(case, '参数')
            checks = get(case, '检查点')
            values = get(case, '取全局变量')
            state = get(case, '是否测试')
            if not headers:
                headers = {}
            if not data:
                data = {}

            FUNC_TEMPLATE = """@unittest.skipUnless({state},'state值为0,跳过测试')
class {classes}(unittest.TestCase):
    def test_{id}(self):
        '''{des}'''
        url = '{url}'
        method = Method.{method}
        type = Type.{type}
        headers = {headers}
        client = Client(url=url, method=method, type=type)
        client.set_headers(headers)
        data = {data}
        client.set_data(data)
        client.send()\n"""
            if checks:
                checks = checks.split('&')
                for check in checks:
                    FUNC_TEMPLATE += '        client.%s \n' % check
            if values:
                values = values.split('&')
                for value in values:
                    FUNC_TEMPLATE += '        client.%s \n' % value
            exec(FUNC_TEMPLATE.format(classes=id.upper(), id=id, des=des, url=url, method=method, type=type,
                                      headers=headers, data=data, state=state))
            ADD = 'suite.addTest({case}("test_{id}"))'
            exec(ADD.format(case=id.upper(), id=id))
        title = '%s.html' % time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        fp = open(sys.argv[0] + '\\..\\report\\' + title, 'wb')
        HTMLTestReportCN.HTMLTestRunner(stream=fp, title='接口测试报告', tester='guojl').run(suite)
        fp.close()
        shutil.copyfile(sys.argv[0] + '\\..\\report\\' + title, sys.argv[0] + '\\..\\report\\report.html')

    send_email(sys.argv[0] + '\\..\\report\\' + title)
