"""
Author : xionghhcs
Desc : 爬取豆瓣电影排行榜
Date : 2017-05-16 09:05:33
"""

import multiprocessing
import requests
import json
import xlwt

headers ={
    'Host': 'movie.douban.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                  'AppleWebKit/537.36 (KHTML, like Gecko)' \
                  ' Chrome/58.0.3029.96 Safari/537.36',
    'Referer': 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C%E7%89%87&type=5&interval_id=100:90&action=',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

def getHtml(url):
    try:
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error in getHtml()')
        return ''

def writeToXls(sheet,data,row):
    sheet.write(row,0,data['title'])
    sheet.write(row,1,data['rank'])
    sheet.write(row,2,data['score'])
    sheet.write(row,3,data['vote_count'])
    sheet.write(row,4,data['release_date'])
    sheet.write(row,5,data['url'])
    pass

def main():
    base_url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%%3A90&action=&start=%d&limit=%d'
    limit = 20
    totalNum = 106
    try:
        wb = xlwt.Workbook("douban.xls")
        sheet = wb.add_sheet("fiction-movie")
        sheet.write(0, 0, 'title')
        sheet.write(0, 1, 'rank')
        sheet.write(0, 2, 'score')
        sheet.write(0, 3, 'vote_count')
        sheet.write(0, 4, 'release_date')
        sheet.write(0, 5, 'url')
    except:
        print("error when open xls")
        return
    index = 1
    for start in range(0,106,20):
        if start + limit >106:
            limit = 106-start
        full_url = base_url%(start,limit)
        data = getHtml(full_url)
        if data == '':
            continue
        jsonData = json.loads(data)
        for item in jsonData:
            print(index,item['title'])
            writeToXls(sheet,item,index)
            index +=1
    wb.save("douban.xls")

main()
# wb = xlwt.Workbook("douban.xls")
# sheet = wb.add_sheet("fiction-movie")
# sheet.write(0,0,"熊猫")
# sheet.write(0,1,"2")
# wb.save("douban.xls")




