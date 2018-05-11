# Copyright (C) 2018 GuQiangJs.
# Licensed under https://www.gnu.org/licenses/gpl-3.0.html <see LICENSE file>

# http://rarbg.is/torrents.php?category=14%3B17%3B42%3B44%3B45%3B46%3B47%3B48%3B50%3B51%3B52&page=

import re
import urllib
from bs4 import BeautifulSoup

class movie():
    def __init__(self, name, year, imdb=None,url=None,magnet=None):
        self._name = name
        self._imdb = imdb
        self._year = year
        self._url_magnet={}
        self.add_magnet(url,magnet)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name=value

    def add_magnet(self,url,magnet):
        if url and magnet:
            self._url_magnet[url]=magnet

    def get_all_magnets(self):
        return self._url_magnet.values()

    def remove_magnet(self,url):
        if url and url in self._url_magnet:
            del self._url_magnet[url]

    @property
    def imdb(self):
        return self._imdb

    @imdb.setter
    def imdb(self,value):
        self._imdb=value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self,value):
        self._year=value

class magnet():
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,value):
        self._size=value

    @property
    def upload(self):
        return self._upload

    @upload.setter
    def upload(self,value):
        self._upload=value

    @property
    def hash(self):
        return self._hash

    @hash.setter
    def hash(self,value):
        self._hash=value

    @property
    def torrent(self):
        return self._torrent

    @torrent.setter
    def torrent(self,value):
        self._torrent=value

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self,value):
        self._comment=value

BASE_URL = 'https://thepiratebay.org'
RE_IMDB = re.compile('(http://imdb.com/title/tt\d{7}/)')
RE_M = re.compile('href="(/torrent/.{7})')
RE_TITLE_RAGBG = re.compile('<title>(.*?)</title>')
RE_TITLE_IMDB = re.compile("<meta property='og:title' content=\"(.*?) \((\d{4})\)\" />")
LST = '{0}/browse/200/{1}/3'

_PROXY_HANDLER = urllib.request.ProxyHandler({'https': 'https://127.0.0.1:1080', 'http': 'http://127.0.0.1:1080'})
_OPENER = urllib.request.build_opener(_PROXY_HANDLER)
_OPENER.addheaders = [
#     ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'),
#     ('Accept-Encoding', 'gzip, deflate'),
#     ('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7'),
#     ('Cache-Control', 'max-age=0'),
#     ('Connection', 'keep-alive'),
#     ('Cookie',
#      'q2bquVJn=qCBnZk87; tcc; aby=1; ppu_main_c1e15f9bb40c93d033719a2dc0fd2cc3=1; ppu_sub_c1e15f9bb40c93d033719a2dc0fd2cc3=1'),
#     ('DNT', '1'),
#     ('Host', 'rarbg.is'),
#     ('Upgrade-Insecure-Requests', '1'),
    ('User-Agent',
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')]


def get_context(url, encoding='utf-8'):
    rep = _OPENER.open(url)
    return str(rep.read(), encoding)

def get_movie_list(context):
    lst=BeautifulSoup(context,"lxml").find_all("a")
    result={}
    for l in lst:
        if 'href' in l.attrs and l.attrs['href'].startswith('/torrent'):
            m=re.search(r'(.*?)[\._](\d{4})\.',l.text)
            if m:
                result[movie(m.group(1),m.group(2))]=l.attrs['href']
            # else:
                # print('SKIP:'+l.attrs['href'])
    return result

def get_magnet(url):
    context=get_context(BASE_URL+url)
    m=re.search(r'href="(magnet:.*?)"',context)
    dts=BeautifulSoup(context,'lxml').find_all("dt")
    for dt in dts:
        if dt.name=='size':
            s=_get_next_element(dt,'dd')
        elif dt.name=='uploaded:':
            d=_get_next_element(dt,'dd')

    if m:
        magnet= m.group(1)
    return None

def _get_next_element(ele,next_name):
    if ele and ele.next_element:
        if ele.next_element.name==next_name:
            return ele.next_element.text
        else:
            return _get_next_element(ele.next_element,next_name)
    return None

movies = []
for i in range(10000):
    context = get_context(LST.format(BASE_URL, i))
    movies=get_movie_list(context)
    for k,v in movies.items():
        print('{0} {1} - {2}'.format(k.year,k.name,v))
        magnet=get_magnet(v)
        if magnet:
            k.add_magnet(v,magnet)


    # urls = RE_M.findall(context)
    # if not urls:
    #     break
    # for url in urls:
    #     con_m = get_context('{0}{1}'.format(BASE_URL, url))
    #     # title=RE_TITLE.search(con_m).group(1)
    #     imdb = RE_IMDB.search(con_m).group(1)
    #     com_imdb = get_context(imdb)
    #     m, title, year = RE_TITLE_IMDB(com_imdb).groups()
    #     print('{0} - {1} - {2}'.format(imdb, title, url))
    #     movies.append(movie(url, title, imdb))
