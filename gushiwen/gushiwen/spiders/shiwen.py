# -*- coding: utf-8 -*-
import scrapy
from
from scrapy import FormRequest

from yundm import YDMHttp


class ShiwenSpider(scrapy.Spider):
    name = 'shiwen'
    allowed_domains = ['www.gushiwen.org']

    def start_requests(self):

        # yield 发起FormRequest请求
        url = "https://so.gushiwen.org/user/login.aspx?from="
        # code_url = 'https://so.gushiwen.org/RandCode.ashx'
        code_url = "https://so.gushiwen.org/RandCode.ashx?t=1545967881204?t=1545968030160"
        # 请求验证码
        resp:HTTPResponse = get(code_url)
        code_file_name = 'code.png'
        # 将验证码保存到图片中
        with open(code_file_name,'wb') as f:
            f.write(resp.content)

        # 云达码对象
        yundm = YDMHttp()
        yundm.login()
        cid,result = yundm.decode(code_file_name,1004,30)

        data = {
            'email':'',
            'pwd':'',
            'code':result,
        }
        # 登录后，会产生cookie相关信息
        # 要求开启cookie信息
        yield FormRequest(url,formdata=data,callback=self.parse_login)

    def parse_logined(self,response):
        print("-----登陆成功--------")
        print(response.text)
        print(response.url)