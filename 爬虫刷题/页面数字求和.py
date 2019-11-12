"""
@Time    : 2019/11/8 0008 16:53
@Author  : Linyue
@Email   : l_inyue@163.com
@File    : 页面数字求和.py
@name    ：
"""
import requests
from fake_useragent import UserAgent
from lxml import etree


class Qiuhe_spider(object):
    def __init__(self):
        self.url = 'http://glidedsky.com/level/web/crawler-basic-1'
        self.login = 'http://glidedsky.com/login'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Cookie': "Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1573203080; _ga=GA1.2.70965079.1573203080; _gid=GA1.2.1600021850.1573203080; footprints=eyJpdiI6IitkR0w0Y2RVTWp2RVVudWRxWXA5a3c9PSIsInZhbHVlIjoiZ241eTczXC9CdE9JalFDXC9XR0ZnNzhkRGNpdXdrSjJPVHA4Q1dBMHFtMlJvWklpMUlVRktCMHhyTHZwQXVJVVJ2IiwibWFjIjoiOWZlYjllMGVjZWI5YWQxMDE0MTVhNjRiMmY3MGViMzZiM2FlNjc2ZGMwYjE3ZTVkNmI4MWFiZGY5ZDk2NDlhZiJ9; XSRF-TOKEN=eyJpdiI6IlFlVlBwelhMM0pqcVpWOU9KTGxESUE9PSIsInZhbHVlIjoiaFVNOThnaTRwV3o1S0tGVFBOWVwvK2JuT0NcL3YzRE05K3JSb0Fqc2xTb2V3VTFnWWx5WU5sV0dndkJBMWgyRkZtIiwibWFjIjoiMDRjZDc3OTkxNmMxOTA0YTY4MWE3YTA1Mjk0NWQ3MThkOWMxNWY0ZDBmZDQ1YzMwMTZlNGJiODU5OTM3NzJiZiJ9; glidedsky_session=eyJpdiI6IjM4cTd2dHpPSFIyWVRqS01aelQ0T3c9PSIsInZhbHVlIjoiN1dnUm52dmRvbm5MRnJPN2xHRnk4U1wvUmpodjFOZ1dqRnQzTXpaQnFKWmNxXC9jME1MT293SkN1bWNEMkdtWTF4IiwibWFjIjoiNjg5ZDE1NWU1Mzg2ZmU0ZmFlZGE4NzRiMGRlOWFlODU0MmI0MDllZjFiODkxZTczNmRhZTg0NmI2M2M3YmNmMiJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1573205473; _gat_gtag_UA_75859356_3=1", }

        self.num = 0
        self.data = {
            '_token': '8yds0DU3ryqD2BCC7dgpEnRU2PzcqRUuJbLDqQHC',
            "email": 'l_inyue@163.com',
            'password': 962464,
        }
        self.session = requests.session()

    def get_html(self):
        headers = {
            'Referer': 'http://glidedsky.com/login',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
        # self.session.post(url=self.login, data=self.data, headers=headers)
        html = requests.get(self.url, headers=self.headers)
        return html

    def parse_html(self):
        print(self.headers)
        html = self.get_html()
        print(html.text)
        parse_html = etree.HTML(html.text)
        int_list = parse_html.xpath("//div[@class='col-md-1']//text()")
        for i in int_list:
            self.num += int(i)
        print(self.num)


if __name__ == '__main__':
    qh = Qiuhe_spider()
    qh.parse_html()
