"""
urllib模块
GET请求

状态码:HTTP响应中表示请求结果的3位数字代码(1xx:临时响应 2xx:成功状态 4xx:客户端错误)
原因短语:对状态码的辅助说明
响应头:服务器返回的元数据，用于控制客户端行为或传递附加信息(Content-Type响应体的媒体类型  Content-Length响应体的字节长度)
1.
import urllib error
from urllib import request

url = 'http://www.baidu.com'

def get_request(url):

    try:

        with request.urlopen(url) as f:     #使用 urllib.request.urlopen 方法向 http://www.baidu.com 发送一个 GET 请求。

            data = f.readline()

            print(f"Status:{f.status} {f.reason}")    #响应的状态码和原因短语     使用 getcode() 函数获取网页状态码

            for i,j in f.getheaders():

                print(f"{i}:{j}")     #使用 f.getheaders() 方法获取响应头，并遍历打印每个头字段及其值。

        print(f"Data:{data.decode('UTF-8')}")

    except urllib.error.HTTPError as e:

        if e.code == 404:

            print(404)

def main():

    get_request(url)

if __name__ == "__main__":

    main()

2.
import urllib.error
import urllib.request

url = "https://leetcode.cn/"

def get_request(url):

    try:

        with urllib.request.urlopen(url) as f:

            data = f.read()

            print(f"{f.getcode()}")

        with open("python.py","wb") as f:

            f.write(data)

            print(f"Data:{data.decode('utf-8')}")

    except urllib.error.HTTPError as e:

        if e.code == 404:

            print(404)

def main():

    get_request(url)

if __name__ == "__main__":

    main()


模拟头部信息

import urllib.request
from urllib.request import Request

url = 'https://www.runoob.com/?s='

keyword = 'Python 教程'
key_code = urllib.request.quote(keyword)   #对请求进行编码      解码使用 urllib.request.unquote

url_all = url + key_code

#头部信息
header = {
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

#抓取网页一般需要对headers(网页头信息)进行模拟,这时候需要使用 urllib.request.Request(url, data=None, headers={})
request = urllib.request.Request(url_all,headers = header)

with urllib.request.urlopen(request) as f:

    data = f.read()

    print(f"Data:{data.decode('utf-8')}")

with open("./urllib_test_runoob_search.html","wb") as f:

    f.write(data)


表单 POST 传递数据

import urllib.request
import urllib.parse

url = 'https://www.runoob.com/try/py3/py3_urllib_test.php'  # 提交到表单页面

data = {'name':'RUNOOB', 'tag' : '菜鸟教程'}   # 提交数据

header = {
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 对参数进行编码,解码使用 urllib.parse.urldecode
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url,data,headers = header)   #请求处理

with urllib.request.urlopen(request) as f:

    data = f.read()

    print(f"Date:{data.decode('utf-8')}")

with open("./urllib_test_post_runoob.html","wb") as f:

    f.write(data)


urllib.error模块

1.URLError用于处理程序在遇到问题时会引发此异常.

2.HTTPError是URLError的一个子类,用于处理特殊HTTP错误.


urllib.parse模块

urllib.parse用于解析URL:urllib.parse.urlparse(urlstring, scheme='',fragments=True)
urlstring为字符串的url地址,scheme为协议类型,fragments参数为False,则无法识别片段标识符

from urllib.parse import urlparse

print(urlparse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B"))

#输出的内容是一个元组,包含:协议、位置、路径、参数、查询、判断,可以直接对其中一个进行读取
"""
