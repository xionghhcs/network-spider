import utils
from lxml import etree
import pandas as pd


def clear_content(content):
    content = content.strip('\r\n\t\u3000 ')
    return content


def get_title_url(href_selector, title_selector, first_page_num, max_page_num, main_url, first_page_url, base_url=None,
                  encode=None):
    data = []
    for idx in range(first_page_num, max_page_num + 1):
        print('正在抓取第{}页'.format(idx))
        if idx == first_page_num:
            full_url = first_page_url
        else:
            full_url = main_url.format(idx)
        html = utils.get_html(full_url, encoding=encode)
        if html is not '':
            selector = etree.HTML(html)
            href_list = selector.xpath(href_selector)
            title_list = selector.xpath(title_selector)
            assert len(href_list) == len(
                title_list), 'the length should be same but got href\'length is {} and title\'length is {}'.format(
                len(href_list), len(title_list))
            for href, title in zip(href_list, title_list):
                if base_url is not None:
                    href = base_url + href
                row = (title, href)
                data.append(row)
    return data


def get_title_content(title_href_list, content_selector, encode=None):
    data = []
    all_num = len(title_href_list)
    for idx, item in enumerate(title_href_list):
        print('正在获取内容[{}/{}]'.format(idx, all_num))
        html = utils.get_html(item[1], encoding=encode)
        if html != '':
            try:
                selector = etree.HTML(html)
                webnr = str(selector.xpath(content_selector)[0].xpath('string(.)'))
                webnr = clear_content(webnr)
                data.append([item[0], webnr])
            except:
                print('[Error] : {}'.format(item[0]))
    return data


# if __name__ == '__main__':
def get_zhzyw_data():
    # 准备参数
    href_selector = '//div[@class="ullist01"]/ul/li/a/@href'
    title_selector = '//div[@class="ullist01"]/ul/li/a/text()'
    first_page_num = 1
    max_page_num = 25
    main_url = 'https://www.zhzyw.com/zycs/zyjb/index_{}.html'
    first_page_url = 'https://www.zhzyw.com/zycs/zyjb/index.html'
    base_url = 'https://www.zhzyw.com'

    # 获取titile和对应的url
    title_href = get_title_url(href_selector=href_selector,
                               title_selector=title_selector,
                               first_page_num=first_page_num,
                               max_page_num=max_page_num,
                               main_url=main_url,
                               first_page_url=first_page_url,
                               base_url=base_url)
    # 从title和url中获取content
    content_selector = '//div[@class="webnr"]'
    title_content = get_title_content(title_href, content_selector=content_selector)
    return title_content
    pass


# if __name__ == '__main__':
def get_zhongyoo():
    # 准备参数
    href_selector = '//div[@class="listbox"]//li/a/@href'
    title_selector = '//div[@class="listbox"]//li/a/text()'
    first_page_num = 1
    max_page_num = 15
    main_url = 'http://www.zhongyoo.com/jianding/page_{}.html'
    first_page_url = 'http://www.zhongyoo.com/jianding/'
    base_url = 'http://www.zhongyoo.com'

    # 获取titile和对应的url
    title_href = get_title_url(href_selector=href_selector,
                               title_selector=title_selector,
                               first_page_num=first_page_num,
                               max_page_num=max_page_num,
                               main_url=main_url,
                               first_page_url=first_page_url,
                               base_url=base_url)
    # print(title_href[:10])
    # 从title和url中获取content
    content_selector = '//div[@id="contentText"]'
    title_content = get_title_content(title_href, content_selector=content_selector)
    # print(title_content[:10])
    return title_content
    pass


# if __name__ == '__main__':
def get_med66():
    # 准备参数
    href_selector = '//div[@class="news"]//li/a/@href'
    title_selector = '//div[@class="news"]//li/a/text()'
    first_page_num = 1
    max_page_num = 177
    main_url = 'http://m.med66.com/zhongyaojianding/page{}.shtm'
    first_page_url = 'http://m.med66.com/zhongyaojianding/'
    base_url = None

    # 获取titile和对应的url
    title_href = get_title_url(href_selector=href_selector,
                               title_selector=title_selector,
                               first_page_num=first_page_num,
                               max_page_num=max_page_num,
                               main_url=main_url,
                               first_page_url=first_page_url,
                               base_url=base_url)
    # print(title_href[:10])
    # 从title和url中获取content
    content_selector = '//div[@class="con"]'
    title_content = get_title_content(title_href, content_selector=content_selector)
    # print(title_content[:10])
    return title_content
    pass


# if __name__ == '__main__':
def get_dadou():
    # 准备参数
    href_selector = '//section[@class="main_two"]//dl/a/@href'
    title_selector = '//section[@class="main_two"]//dl//p/text()'
    first_page_num = 1
    max_page_num = 50
    main_url = 'http://m.dadou.net/zyjb/page_{}.html'
    first_page_url = 'http://m.dadou.net/zyjb/'
    base_url = 'http://m.dadou.net'

    # 获取titile和对应的url
    title_href = get_title_url(href_selector=href_selector,
                               title_selector=title_selector,
                               first_page_num=first_page_num,
                               max_page_num=max_page_num,
                               main_url=main_url,
                               first_page_url=first_page_url,
                               base_url=base_url)
    # print(title_href[:10])
    # 从title和url中获取content
    content_selector = '//div[@class="content_main"]'
    title_content = get_title_content(title_href, content_selector=content_selector)
    # print(title_content[:10])
    return title_content
    pass


# if __name__ == '__main__':
def get_jk3721():
    # 准备参数
    href_selector = '//section[@class="main_two"]//dl/a/@href'
    title_selector = '//section[@class="main_two"]//dl//dt//p/text()'
    first_page_num = 1
    max_page_num = 10
    main_url = 'http://wap.jk3721.com/html/zycs/zyjb/list_1069_{}.html'
    first_page_url = 'http://wap.jk3721.com/html/zycs/zyjb/list_1069_1.html'
    base_url = None

    # 获取titile和对应的url
    title_href = get_title_url(href_selector=href_selector,
                               title_selector=title_selector,
                               first_page_num=first_page_num,
                               max_page_num=max_page_num,
                               main_url=main_url,
                               first_page_url=first_page_url,
                               base_url=base_url)
    # print(title_href[:10])
    # 从title和url中获取content
    content_selector = '//div[@class="content"]'
    title_content = get_title_content(title_href, content_selector=content_selector)
    # print(title_content[:10])
    return title_content
    pass


# if __name__ == '__main__':
def get_zhongyibaodian():
    # 准备参数
    href_selector = '//ul[@class="a-b"]//li/a/@href'
    title_selector = '//ul[@class="a-b"]//li/a/text()'
    first_page_num = 1
    max_page_num = 1
    main_url = 'http://zhongyibaodian.com/TCM/zhongyaojianbie-590-1.html'
    first_page_url = 'http://zhongyibaodian.com/TCM/zhongyaojianbie-590-1.html'
    base_url = 'http://zhongyibaodian.com'

    # 获取titile和对应的url
    title_href = get_title_url(href_selector=href_selector,
                               title_selector=title_selector,
                               first_page_num=first_page_num,
                               max_page_num=max_page_num,
                               main_url=main_url,
                               first_page_url=first_page_url,
                               base_url=base_url)
    print('Url num : {}'.format(len(title_href)))
    print('Sample(the last 5 url) : {}'.format(title_href[-5:]))
    # 从title和url中获取content
    content_selector = '//div[@class="spider"]'
    title_content = get_title_content(title_href, content_selector=content_selector)
    # print(title_content[:10])
    return title_content
    pass


# if __name__ == '__main__':
def get_360bzl():
    # 准备参数
    href_selector = '//div[@class="Con-list"]//div[@class="list-nf"]/a/@href'
    title_selector = '//div[@class="Con-list"]//div[@class="list-nf"]/div[@class="list-box fl"]//a/text()'
    first_page_num = 1
    max_page_num = 162
    main_url = 'http://zyc.360bzl.com/list265-{}.html'
    first_page_url = 'http://zyc.360bzl.com/list265.html'
    base_url = None

    # 获取titile和对应的url
    title_href = get_title_url(href_selector=href_selector,
                               title_selector=title_selector,
                               first_page_num=first_page_num,
                               max_page_num=max_page_num,
                               main_url=main_url,
                               first_page_url=first_page_url,
                               base_url=base_url)
    # print('Url num : {}'.format(len(title_href)))
    # print('Sample(the last 5 url) : {}'.format(title_href[-5:]))
    # 从title和url中获取content
    content_selector = '//div[@class="art_text"]'
    title_content = get_title_content(title_href, content_selector=content_selector)
    # print(title_content[:10])
    return title_content
    pass


# if __name__ == '__main__':
def get_cn939():
    # 准备参数
    href_selector = '//div[@class="listbox"]//ul//a/@href'
    title_selector = '//div[@class="listbox"]//ul//a/text()'
    first_page_num = 1
    max_page_num = 1
    main_url = 'http://www.cn939.com/zysc/zyjb/list-{}.html'
    first_page_url = 'http://www.cn939.com/zysc/zyjb/list.html'
    base_url = 'http://www.cn939.com'

    # 获取titile和对应的url
    title_href = get_title_url(href_selector=href_selector,
                               title_selector=title_selector,
                               first_page_num=first_page_num,
                               max_page_num=max_page_num,
                               main_url=main_url,
                               first_page_url=first_page_url,
                               base_url=base_url)
    # print('Url num : {}'.format(len(title_href)))
    # print('Sample(the last 5 url) : {}'.format(title_href[-5:]))
    # 从title和url中获取content
    content_selector = '//div[@id="fontzoom"]'
    title_content = get_title_content(title_href, content_selector=content_selector)
    # print(title_content[:10])
    return title_content
    pass


# if __name__ == '__main__':
def get_1cool():
    # 准备参数
    href_selector = '//div[@id="content"]//ul[@id="listul"]//li/a/@href'
    title_selector = '//div[@id="content"]//ul[@id="listul"]//li/a/text()'
    first_page_num = 1
    max_page_num = 6
    main_url = 'http://www.1cool.cn/class.asp?id=113&page={}'
    first_page_url = 'http://www.1cool.cn/class.asp?id=113'
    base_url = 'http://www.1cool.cn'

    # 获取titile和对应的url
    title_href = get_title_url(href_selector=href_selector,
                               title_selector=title_selector,
                               first_page_num=first_page_num,
                               max_page_num=max_page_num,
                               main_url=main_url,
                               first_page_url=first_page_url,
                               base_url=base_url)
    print('Url num : {}'.format(len(title_href)))
    print('Sample(the last 5 url) : {}'.format(title_href[-5:]))
    # 从title和url中获取content
    content_selector = '//div[@id="content"]'
    title_content = get_title_content(title_href, content_selector=content_selector)
    print(title_content[:10])
    return title_content
    pass


# if __name__ == '__main__':
def get_39yst():
    # 准备参数
    href_selector = '//div[@class="column_list"]//dl/dd/a/@href'
    title_selector = '//div[@class="column_list"]//dl/dd/a/@title'
    first_page_num = 1
    max_page_num = 11
    main_url = 'http://www.39yst.com/jianding/list_273_{}.shtml'
    first_page_url = 'http://www.39yst.com/jianding/list_273_1.shtml'
    base_url = None

    # 获取titile和对应的url
    title_href = get_title_url(href_selector=href_selector,
                               title_selector=title_selector,
                               first_page_num=first_page_num,
                               max_page_num=max_page_num,
                               main_url=main_url,
                               first_page_url=first_page_url,
                               base_url=base_url,
                               encode='utf-8')
    print('Url num : {}'.format(len(title_href)))
    print('Sample(the last 5 url) : {}'.format(title_href[-10:]))
    # 从title和url中获取content
    content_selector = '//div[@class="article-content"]'
    title_content = get_title_content(title_href[:12], content_selector=content_selector, encode='utf-8')
    content_selector = '//div[@id="content"]'
    title_content += get_title_content(title_href[12:], content_selector=content_selector, encode='utf-8')
    print('Total content num : {}'.format(len(title_content)))
    # print(title_content[:10])
    return title_content
    pass


if __name__ =="__main__":
    title_content = []
    print('抓取 zhzyw...')
    title_content += get_zhzyw_data()
    print('抓取 zhongyoo...')
    title_content += get_zhongyoo()
    print('抓取 med66...')
    title_content += get_med66()
    print('抓取 dadou...')
    title_content += get_dadou()
    print('抓取 jk3721')
    title_content += get_jk3721()
    print('抓取 zhongyibaodian...')
    title_content += get_zhongyibaodian()
    print('抓取 360bzl...')
    title_content += get_360bzl()
    print('抓取 cn939...')
    title_content += get_cn939()
    print('抓取 1cool...')
    title_content += get_1cool()
    print('抓取 39yst...')
    title_content += get_39yst()
    data = pd.DataFrame(title_content, columns=['title', 'content'])
    file_name = 'data.csv'
    data.to_csv(file_name, index=False)
    print('Data save at : {}'.format(file_name))
    print('Total data : {}'.format(len(title_content)))
    pass