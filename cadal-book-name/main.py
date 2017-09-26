"""
Author : xionghh
"""

import requests
from lxml import etree
import pandas as pd
import sys
import getopt

def get_html(url):
    """
    # Description
        通过get方法获取html网页内容
    # Arguments
        url:目标网页url
    # Returns
        html:字符串形式的网页内容
    """
    request_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Host': 'www.cadal.zju.edu.cn',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
    }
    try:
        r = requests.get(url,headers=request_headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error when get url:[%s]'%url)
        return ''



def post_html(url,post_data):
    """
    # Description
        以post方式获取目标网站搜索结果
    # Arguments
        url:链接
        post_data: 需要post到服务器的数据，包含搜索的关键字、页码等信息
    # Returns
        r.text: post后服务器返回的html页面
    """
    request_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Host': 'www.cadal.zju.edu.cn',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
    }
    try:
        r = requests.post(url,data=post_data,headers=request_headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error when post url:[%s]'%url)
        return ''


def get_all_page_num(input_str):
    """
    # Description
        从页面中找到“共x页”内容，从中得到页数信息
    # Arguments
        input_str:字符串信息为'第x页 共y页'
    # Returns
        res:返回y
    """
    input_str = input_str.strip()
    start = input_str.find('共')
    end = input_str.rfind('页')
    res = input_str[start + 1:end]
    return int(res)



def get_content(html):
    """
    # Description
        获取页面信息[丢弃]
    """
    selector = etree.HTML(html)
    product_title_list = selector.xpath('//div[@class="product"]/div/p[@class="productTitle"]/a/abbr/text()')
    product_author_list = selector.xpath('//div[@class="product"]/div/p[@class="productAuthor"]/span/font/abbr/text()')
    product_press_list = selector.xpath('//div[@class="product"]/div/p[@class="productPress"]/span/font/abbr/text()')
    if len(product_title_list)==0 or len(product_author_list)==0 or len(product_press_list)==0:
        print('result is empty')
        return None
    # 确保数据对齐
    if len(product_title_list)==len(product_author_list) and len(product_title_list)==len(product_press_list) and len(product_author_list)==len(product_press_list):
        res = list(zip(product_title_list, product_author_list, product_press_list))
        return res
    print('data error')
    print(product_title_list)
    return None



# @return : tuple
def get_detail_content(book_id,html):
    """
    # Description
        从html中获取书名、作者、出版社等书籍详细信息，并以tuple的形式返回
    # Arguments
        book_id:book_id从外部粗传入，也是书籍信息的一部分
        html:网页页面
    # Returns
        (book_id,book_name,author,publisher,pubdate,subject,description,other,type)：
            书籍详细信息
    """
    selector = etree.HTML(html)

    book_name = ''
    res_list = selector.xpath('//div[@id="bookinfo"]/span[@id="span_title_val"]/text()')
    if len(res_list)>0:
        book_name = res_list[0]
        book_name = book_name.strip()
        book_name = book_name.replace('\t', '')
        book_name = book_name.replace('\n', '')
    # print('book name:%s'%book_name)

    author=''
    res_list = selector.xpath('//div[@id="bookinfo"]/span[@id="span_author_val"]/text()')
    if len(res_list)>0:
        author = res_list[0]
        author = author.strip()
        author = author.replace('\r','')
        author = author.replace('\n','')
    # print('author:%s'%author)

    publisher = ''
    res_list = selector.xpath('//div[@id="bookinfo"]/span[@id="span_publisher_val"]/text()')
    if len(res_list) > 0:
        publisher = res_list[0]
        publisher = publisher.strip()
        publisher = publisher.replace('\r','')
        publisher = publisher.replace('\n','')
    # print('publisher:%s' % publisher)

    pubdate = ''
    res_list = selector.xpath('//div[@id="bookinfo"]/span[@id="span_pubdate_val"]/text()')
    if len(res_list) > 0:
        pubdate = res_list[0]
        pubdate = pubdate.strip()
        pubdate = pubdate.replace('\r','')
        pubdate = pubdate.replace('\n','')
    # print('pubdate:%s' % pubdate)

    subject = ''
    res_list = selector.xpath('//div[@id="bookinfo"]/span[@id="span_subject_val"]/text()')
    if len(res_list) > 0:
        subject = res_list[0]
        subject = subject.strip()
        subject = subject.replace('\r', '')
        subject = subject.replace('\n', '')
    # print('subject:%s' % subject)

    description = ''
    res_list = selector.xpath('//div[@id="bookinfo"]/span[@id="span_description_val"]/text()')
    if len(res_list) > 0:
        description = res_list[0]
        description = description.strip()
        description = description.replace('\r','')
        description = description.replace('\n','')
    # print('description:%s' % description)

    other = ''
    res_list = selector.xpath('//div[@id="bookinfo"]/span[@id="span_other_val"]/text()')
    if len(res_list) > 0:
        other = res_list[0]
        other = other.strip()
    # print('other:%s' % other)

    type = ''
    res_list = selector.xpath('//div[@id="bookinfo"]/span[@id="type"]/text()')
    if len(res_list) > 0:
        type = res_list[0]
        type = type.strip()
    return (book_id,book_name,author,publisher,pubdate,subject,description,other,type)

def get_url_list(html):
    selector = etree.HTML(html)
    url_in_html = selector.xpath('//div[@class="product"]/div/p[@class="productOther"]/span/a[1]/@href')
    return url_in_html

def main(in_book_list,version):
    book_name_list = []
    if in_book_list is not None:
        book_name_list = in_book_list
    else:
        print('key word list is empty')
        sys.exit()
    url = "http://www.cadal.zju.edu.cn/search/bookSearch"
    host_url = 'http://www.cadal.zju.edu.cn'
    # 保存所有书籍详情页面的url链接
    url_list=[]
    # 遍历词表
    for query in book_name_list:
        form_data = {
            'query': query,
            'booktype': 'book',
            'pageNo': 1,
            'typeBtn': '全部',
            'tagBtn': '',
            'publisher': '',
            'querytype': 'All'
        }
        html = post_html(url,form_data)
        if html =='':
            print('html is empty')
            continue
        else:
            selector = etree.HTML(html)
            page_all_num = selector.xpath('//div[@id="moreresults"]/div[last()]/text()')
            if len(page_all_num)>0:
                page_all_num = page_all_num[0]
                # res.to_csv('test.csv',header=['书名','作者','出版社'],index=False,encoding='utf-8')
                # 遍历页数,获取所有页面的书籍详情url
                page_num = get_all_page_num(page_all_num)
                for pageNo in range(1,page_num+1):
                    # if pageNo==4:
                    #     break
                    form_data = {
                        'query': query,
                        'booktype': 'book',
                        'pageNo': pageNo,
                        'typeBtn': '全部',
                        'tagBtn': '',
                        'publisher': '',
                        'querytype': 'All'
                    }
                    print('关键字:%s 第%d页...'%(query,pageNo))
                    html = post_html(url,form_data)
                    if html != '':
                        page_res = get_url_list(html)
                        for item in page_res:
                            url_list.append(host_url + item)
    # 将书籍详细url信息存至本地
    url_list_df = pd.DataFrame(url_list)
    url_list_df.to_csv('book_detail_url_list_'+ version +'.csv',header=False,index=False)

    # 一行表示一本书的详细信息，分别有id，书名，作者，出版社，出版日期，关键字，描述，其他，类型，加工单位
    detail_item_list=[]
    error_url_list = []
    index = 0
    for each_url in url_list:
        index +=1
        print('抓取第 %d 本书详细信息' % index)
        book_id = each_url.split('/')[-1]
        html = get_html(each_url)
        # 这里还有一种情况需要考虑，如果返回的是别人的错误提示页面，也就是页面中没有书籍详细信息，这时会插入一个空的tuple
        # 这里没有做判断和处理
        if html != '':
            detail_info = get_detail_content(book_id,html)
            detail_item_list.append(detail_info)
        else:
            error_url_list.append(each_url)

    # 将出错链接保存至本地，方便对出错信息进行再次抓取
    error_url_list_df = pd.DataFrame(error_url_list)
    error_url_list_df.to_csv('book_detail_url_list_error_'+version+'.csv',header=False,index=False)

    print('正在保存书籍信息至本地...')
    res_df = pd.DataFrame(detail_item_list)
    res_df = res_df.drop_duplicates()
    # 插入新的一列:是否需要
    res_df.insert(0,'是否需要','')
    res_df.to_csv('cadal-'+version+'.csv',header=['是否需要','id','书名','作者','出版社','出版日期','关键字','描述','其他','类型'],index=False,encoding='UTF-8')
    print('已写入本地')

    print('报表:')
    print('抓取书本信息条数: %d' %len(res_df))
    print('错误连接数目: %d' % len(error_url_list_df))


file_name = None
ver = None

# 获取参数
try:
    options, args = getopt.getopt(sys.argv[1:], 'hk:v:')
except:
    sys.exit()
# 接入参数
for name, value in options:
    if name in ['-h']:
        print('try to use python main.py -k key_word_file_name -v version to run this script')
        print('Note:')
        print(' -k:follow the key word file name(without .csv)')
        print(' -v:follow the version (the output files will consist of this string)')
        sys.exit()
        pass
    elif name in ['-k']:
        file_name = value
    elif name in ['-v']:
        ver = value

if file_name is None or ver is None:
    print('parameters is required,use -h to show the help!')
    sys.exit()

try:
    key_word_list = pd.read_csv(file_name + '.csv', encoding='UTF8')
    key_word_list = key_word_list.values[:,0].tolist()
except:
    print('open file %s error' % (file_name + '.csv'))
    sys.exit()

main(key_word_list,ver)
