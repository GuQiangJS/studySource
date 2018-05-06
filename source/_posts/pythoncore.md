---
title: Python 核心编程
date: 2018-05-05 22:06:54
tags:
 - 编程
 - Python
photos:
 - /2018/05/05/pythoncore/pythoncore.png
categories:
 - 编程
 - Python
出版社: 人民邮电出版社
ISBN: 9787115414779
出版时间: 2016-05-01
description: <!—more—->
---

#### [re](https://docs.python.org/3.6/library/re.html?highlight=re#module-re) - 正则表达式

>  [`re.compile`](https://docs.python.org/3.6/library/re.html?highlight=re#re.compile) 为正则表达式提供了预编译功能。如果程序在执行过程中需要多次调用到正则表达式对象，那么采用预编译可以提升执行性能。

[`search()`](https://docs.python.org/3.6/library/re.html?highlight=re#re.regex.search) 和 [`match()`](https://docs.python.org/3.6/library/re.html?highlight=re#re.regex.match) 的不同之处在于 [`search()`](https://docs.python.org/3.6/library/re.html?highlight=re#re.regex.search) 会在**任意位置**进行匹配。

#### [socket](https://docs.python.org/3.6/library/socket.html?highlight=socket#module-socket) - 低级网络接口

1. 基于文件的 Socket：[`socket.AF_UNIX`](https://docs.python.org/3.6/library/socket.html?highlight=socket#socket.AF_UNIX)
2. 基于网络的 Socket：[`socket.AF_INET`](https://docs.python.org/3.6/library/socket.html?highlight=socket#socket.AF_INET)


1. 有链接的Socket(**TCP**)：[`socket.SOCK_STREAM`](https://docs.python.org/3.6/library/socket.html?highlight=socket#socket.SOCK_STREAM)
2. 无链接的Socket(**UDP**)：[`socket.SOCK_DGRAM`](https://docs.python.org/3.6/library/socket.html?highlight=socket#socket.SOCK_DGRAM)

`tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`

{% codeblock 服务端 tsTserv3.py lang:python %}
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        #tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))
    
    tcpCliSock.close()
tcpSerSock.close()
{% endcodeblock %}

{% codeblock 客户端 tsTclnt3.py lang:python %}
from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()
{% endcodeblock %}