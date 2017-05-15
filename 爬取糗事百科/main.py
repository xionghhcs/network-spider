"""
Author : xionghhcs
Desc : 糗事百科“文字”模块抓取练习
Date : 2017-05-15 20:02:47
"""

import requests
from lxml import etree
import time
import random
import codecs

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/58.0.3029.96 Safari/537.36'
}

def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error in getHtml()')
        return ''

def writeToFile(f,item):
    try:
        f.writelines('用户名:'+item['user_name']+'\n')
        f.writelines('段子:'+item['user_content']+'\n\n')
    except:
        print('error in writeToFile()')


def main():
    base_url = 'http://www.qiushibaike.com/text/page/%d/?s=4982836'
    try:
        f = codecs.open('qiushi.txt','a','utf-8')
    except:
        print('erroe when open file')
        return
    for page_num in range(1,35+1):
        # 随机延时
        sleep_time = random.uniform(0,30)
        time.sleep(sleep_time)
        if page_num == 1:
            full_url = 'http://www.qiushibaike.com/text/'
        else:
            full_url = base_url % page_num
        print(str(page_num)+' crawl url : ',full_url)
        html = getHtml(full_url)
        if html == '':
            continue
        selector = etree.HTML(html)
        div_list = selector.xpath('//div[@class="article block untagged mb15"]')
        for item in div_list:
            data_item={}
            user_names = item.xpath('div[@class="author clearfix"]/a/@title')
            user_contents = item.xpath('*/div[@class="content"]/span')
            data_item['user_name'] = '匿名用户'
            if len(user_names)>0:
                data_item['user_name'] = user_names[0]
            data_item['user_content'] = ""
            if len(user_contents)>0:
                data_item['user_content'] = user_contents[0].xpath('string(.)')
            writeToFile(f,data_item)
    print('finish ...')
    f.close()
    pass

main()
