import random

import requests
from lxml import etree

proxies = [
    "https://220.168.52.245:55255",
    "https:119.101.117.45:9999",

]

def random_proxy():
    return random.choice(proxies)

def test_proxy():
    for ip_address in proxies:
        ip = ip_address.split("//")[-1]
        if ip_address.split(':')[0] == 'http':
            url = 'http://ip.tool.chinaz.com'
            resp = requests.get(url,proxies={'http':ip})
            et = etree.HTML(resp.text)
            proxy_ip = et.xpath('//dd[@class="fz24"]/text()')[0]

        else:
            url = 'https://ip.cn'

