"""
@Time    : 2019/11/8 0008 17:34
@Author  : Linyue
@Email   : l_inyue@163.com
@File    : 多个页面爬取.py
@name    ：
"""
import time
import random

import requests
from lxml import etree
from threading import Thread

num = 0
url = 'http://glidedsky.com/level/web/crawler-basic-2?page={}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Cookie': "_ga=GA1.2.70965079.1573203080; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1573203080,1573434098; _gid=GA1.2.704265888.1573434098; footprints=eyJpdiI6ImtMUEdsNnBXRVU5amFBS1BzYVwvZzdRPT0iLCJ2YWx1ZSI6IjJlb3NCQUQzd1NsSmY1OWlqZkpPNjZabEYwWmpkbFpSRW9aTW9jeTFXa01PYWhOYVRiN1o3RzhpclwvaDM4aVBlIiwibWFjIjoiMzRmZjczYjI2NmY2NGZmNTZmODQwNjBmZGJmZmE0MmY1MTk5YzY1ZTIzMjRjY2JjOThjYjllMDBjNDllYTE4MiJ9; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IndZZmpMdkx1UGFkdmJadlVhd3d6Mmc9PSIsInZhbHVlIjoiY2VNZXVRZjI1T3JcLzZIVWJyK3l1WDlpRnBpbEFDYWlHYmV5bUFvRkVvN2tQaURqckRxaDNkRjdtVkJGcnhDN3RXMWcrM003K2NrNHdNcHFqRDQ2bTRSc3NNUU40OFZqZHRsbFM3d3RGWDhoMG5DY1pYdEcxXC9QeGZUZ05VbnhxYXcwOHR3SElUa0JKZkFjdzUrM0tPc1cxcVIxMlpqbUd4OFdXK0tSUjJaOGs9IiwibWFjIjoiNTE3MWJkZWExNTM2MDc3NzgyNzc4NmMyYTVhNjllYzVkNTI3ZTMwYjFhMTUxZDlkNDhkNWMyNGY3NTQ0NWNmNyJ9; XSRF-TOKEN=eyJpdiI6IlZqNjluXC9PRTRpd2M1TEFlWjBycytBPT0iLCJ2YWx1ZSI6ImEwbm9XUlJDa0RcL3dROUcyNWVHd2JDXC96T3M3dStPUjhHdzMyNHFSWXpcL1FyTGlEUDFwcGQ5akxTQ1dWNWRpUVwvIiwibWFjIjoiYjRkMDc0ZTc3YjFlN2Y2MTcyOTgwODc0ZjNmMTY1NWI4Y2M5NDE3MWVlZmUzMWFkYzA3ZDJlNmMxMTFmM2IwMSJ9; glidedsky_session=eyJpdiI6InVHc2VFbnpSVm5zSDhDcm5IWUVlb2c9PSIsInZhbHVlIjoibjRYdjVnTkFpdml2YVZLdDFaeGRSZTBmUXg4czlqaHRuY1ZjVlFUMjdwYVpqdEcxVk41aXpSdkRFY050Tk53MSIsIm1hYyI6IjBiY2YxOGIzNjk4Y2ZlMmY1YmY2NTBlMjUxZWUxZGMyZjI2ZDljZWJhZjViMzM1MjJhZGQ4YmQ3NmQxNzgyN2IifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1573434135",
}


def num_num(i):
    html = requests.get(url.format(i), headers=headers)

    parse_html = etree.HTML(html.text)
    int_list = parse_html.xpath("//div[@class='col-md-1']//text()")
    for i in int_list:
        global num
        num += int(i.strip())


t_list = []
for i in range(1, 1001):
    num_num(i)
    print(num)
    # t.start()
    # t_list.append(t)
print(num)
# for i in t_list:
#     time.sleep(0.5)
#     i.join()
