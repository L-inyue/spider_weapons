"""
@Time    : 2019/11/11 0011 9:17
@Author  : Linyue
@Email   : l_inyue@163.com
@File    : session登陆.py
@name    ：session登陆
"""
import requests
from lxml import etree

# 1.先POST（把用户名和密码post到一个地址中）
post_url = 'http://glidedsky.com/login'
post_data = {
    'email': 'l_inyue@163.com',
    'password': '962464'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Referer': 'http://glidedsky.com/login'
}
# 实例化session对象
session = requests.session()
session.post(
    url=post_url,
    data=post_data,
    headers=headers
)
# 2.再get（访问需要登录后才能访问的页面）
url = 'http://glidedsky.com/'
html = session.get(url, headers=headers).text
print(html)
parse_html = etree.HTML(html)
result = parse_html.xpath(
    "//tr[@class='d-flex'][1]/td[@class='col-8']//text()"
)
print(result)
