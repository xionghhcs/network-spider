"""
Author : xionghhcs
Desc : 模拟登陆豆瓣
Date : 2017-05-16 18:00:33
"""
import requests
from lxml import etree

'''
获取登陆页面的验证码图片和登陆id标识
'''
def getCaptchaImage(html):
    try:
        selector = etree.HTML(html)
        imgUrl = selector.xpath('//img[@id="captcha_image"]/@src')
        #获得captcha-id
        url = imgUrl[0]
        pos = url.find("id=")
        captcha_id = url[pos+3:pos+30]
        img = requests.get(url).content
        f = open("captcha.jpg",'wb')
        f.write(img)
        f.close()
        return captcha_id
    except:
        print('error in getCaptchaImage()')
        return ""

post_data={
    'source':'None',
    'redir':'https://www.douban.com',
    'form_email':'xllxhh@126.com',
    'form_password':'xhh1314521',
    'captcha-solution':'stiff',
    'captcha-id':'76KRnOW3uaf4egLb4YXiqzUW:en',
    'login':'登录'
}

url = 'https://www.douban.com/accounts/login?'
session = requests.session()
r = session.get(url)
captcha_id=getCaptchaImage(r.text)
captcha = input("验证码:")
post_data['captcha-solution']=captcha
post_data['captcha-id']=captcha_id
r = session.post(url,data=post_data)
#访问个人主页，验证是否登陆成功
r = session.get("https://www.douban.com/people/137322152/")
print(r.text)
