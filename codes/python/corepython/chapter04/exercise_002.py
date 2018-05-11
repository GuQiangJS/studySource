# Copyright (C) 2018 GuQiangJs.
# Licensed under https://www.gnu.org/licenses/gpl-3.0.html <see LICENSE file>

import os
import urllib.request
from bs4 import BeautifulSoup


if not os.path.exists('url.txt'):
    proxy_handler = urllib.request.ProxyHandler({'https': 'https://127.0.0.1:1080'})
    opener=urllib.request.build_opener(proxy_handler)
    response=opener.open('https://zh.wikipedia.org/wiki/Python')
    context=str(response.read(),'utf-8')
    with open('url.txt',mode='wt+',encoding='utf-8') as file:
        file.write(context)

with open('url.txt',encoding='utf-8') as file:
    context=file.read()

# print(context)
soup=BeautifulSoup(context)
lst=soup.find_all("a")
for l in lst:
    if 'href' in l.attrs and l.attrs['href'].startswith('/wiki/'):
        print(l)