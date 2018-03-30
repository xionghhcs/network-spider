
# 说明

该文件夹下保存用于抓取中药鉴别相关信息的代码，爬取的网站主要有：

| 网站名       | url                                                      |
| ------------ | -------------------------------------------------------- |
| 中华中医网   | http://www.zhzyw.org/zycs/zyjb/index.html                |
| 中药查询     | http://www.zhongyoo.com/jianding/                        |
| 医学教育网   | http://m.med66.com/zhongyaojianding/                     |
| 大豆网       | http://m.dadou.net/zyjb/                                 |
| 721健康知识  | http://wap.jk3721.com/html/zycs/zyjb/list_1069_1.html    |
| 中医宝典     | http://zhongyibaodian.com/TCM/zhongyaojianbie-590-1.html |
| 宝芝林中药网 | http://zyc.360bzl.com/list265.html                       |
| 古方中医网   | http://www.cn939.com/zysc/zyjb/list-9.html               |
| 医酷中国     | http://www.1cool.cn/class.asp?id=113                     |
| 三九养生堂   | http://www.39yst.com/jianding/                           |

# 依赖

下面是该程序的一些依赖库

- lxml
- pandas
- requests

# 使用

直接在控制台执行

···
python main.py
···

待抓取结束后，会在当前目录下生成data.csv文件，保存了title和对应content内容
