"""
Author : xionghhcs
Desc : xpath实践，爬取百度贴吧某帖子回复
Date : 2017-05-15 10:31:57
"""

from lxml import etree
import requests
import json
import codecs

def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error in getHtml()')
        return None

def writeToFile(fileHandler,content):
    try:
        fileHandler.writelines(u'用户ID:' + content['user_id'] + '\n')
        fileHandler.writelines(u'用户名:' + content['user_name'] + '\n')
        fileHandler.writelines(u'评论内容:' + content['comment'] + '\n')
        fileHandler.writelines(u'评论时间:' + content['date'] + '\n\n')
    except:
        print('error when write into file')

def main():
    base_url = 'http://tieba.baidu.com/p/3522395718?pn='
    pageNum = 1
    urlList = []
    #生成url链表
    for page_num in range(1,21):
        full_url = base_url + str(page_num)
        urlList.append(full_url)
    try:
        f = codecs.open('comments.txt', 'a',encoding='utf-8')
    except:
        print('error when open file')
        return None

    for url in urlList:
        print('crawl page ',url)
        html = getHtml(url)
        if html == None:
            continue
        selector = etree.HTML(html)
        #取出评论的每个块
        fragments = selector.xpath('//*[@id="j_p_postlist"]/div')
        for item in fragments:
            data_file = item.xpath('@data-field')
            user_info_json = json.loads(data_file[0].replace('&quot',''))
            user_comment = item.xpath('div[@class="d_post_content_main"]/div/cc/div/text()')
            if len(user_comment) == 0:
                continue
            comment = user_comment[0].lstrip()
            commentItem={ }
            commentItem['user_id'] = str(user_info_json['author']['user_id'])
            commentItem['user_name'] = user_info_json['author']['user_name']
            commentItem['date'] = user_info_json['content']['date']
            commentItem['comment'] = comment
            #写入到文件中
            writeToFile(f,commentItem)
    print('crawl tieba finish...')
    f.close()

main()

# html = getHtml('http://tieba.baidu.com/p/3522395718?pn=1')
# selector = etree.HTML(html)
# fragments = selector.xpath('//*[@id="j_p_postlist"]/div')
# data_field = fragments[0].xpath('@data-field')
# user_info_json =json.loads(data_field[0])
# print(user_info_json['author']['user_id'])
# print(user_info_json['author']['user_name'])
# content = fragments[3].xpath('')
# print(content[0].lstrip())


