# coding=utf-8
#模拟登入acm fzu但是一直失败 呜呜
import gzip
import http.cookiejar
import urllib
import urllib.request
import urllib.request

from setuptools.compat import BytesIO

headers = [('Content-Type', 'application/x-www-form-urlencoded'), ('Connection', 'keep-alive'), ('DNT', '1'),
           ('Cache-Control', 'no-cache'), ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'),
           ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'),

           ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
           ('Accept-Encoding', 'gzip, deflate'),
           ('Host', 'zhihu.com'), ('Upgrade-Insecure-Requests', '1')]

print(headers)
data = {'uname': 'zeghaun', 'password': 'abc123', "submit": "Submit"}


class Spider(object):
    def __init__(self, head, post_data):
        # 初始化类，并建立cookies值
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        opener.addheaders = head
        urllib.request.install_opener(opener)
        self.post_data = urllib.parse.urlencode(post_data).encode('UTF-8')

    def login(self, loginurl, encoding='utf-8'):
        # 模拟登陆
        request = urllib.request.Request(loginurl, self.post_data)
        content = self.zip_to_encode_html(request, encoding)
        return content

    def get_html(self, pageurl, encoding='utf-8'):
        # 获取目标网站任意一个页面的html代码
        request = urllib.request.Request(pageurl)
        content = self.zip_to_encode_html(request, encoding)
        return content

    def get_head_cookies(self, pageurl, encoding='utf-8'):
        request = urllib.request.Request(pageurl)
        response = urllib.request.urlopen(request)
        print(response.info())

    def zip_to_encode_html(self, request, encoding='utf-8'):
        response = urllib.request.urlopen(request)

        if response.info().get('Content-Encoding') == 'gzip':
            gzip_f = gzip.GzipFile(fileobj=BytesIO(response.read()))
            content = gzip_f.read()
        else:
            content = response.read()
        return content.decode(encoding)


if __name__ == "__main__":
    x = Spider(headers, data)

