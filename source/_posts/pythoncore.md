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

### 正则表达式

#### [`re`](https://docs.python.org/3.5/library/re.html?highlight=re#module-re) — Regular expression operations

>  [`re.compile`](https://docs.python.org/3.6/library/re.html?highlight=re#re.compile) 为正则表达式提供了预编译功能。如果程序在执行过程中需要多次调用到正则表达式对象，那么采用预编译可以提升执行性能。

If you want to locate a match anywhere in *string*, use [`search()`](https://docs.python.org/3.6/library/re.html?highlight=re#re.regex.search) instead (see also [search() vs. match()](https://docs.python.org/3.6/library/re.html?highlight=re#search-vs-match)).

### 网络编程

#### [socket](https://docs.python.org/3.6/library/socket.html?highlight=socket#module-socket) - 低级网络接口

1. 基于文件的 Socket：[`socket.AF_UNIX`](https://docs.python.org/3.6/library/socket.html?highlight=socket#socket.AF_UNIX)
2. 基于网络的 Socket：[`socket.AF_INET`](https://docs.python.org/3.6/library/socket.html?highlight=socket#socket.AF_INET)


1. 有链接的Socket(**TCP**)：[`socket.SOCK_STREAM`](https://docs.python.org/3.6/library/socket.html?highlight=socket#socket.SOCK_STREAM)
2. 无链接的Socket(**UDP**)：[`socket.SOCK_DGRAM`](https://docs.python.org/3.6/library/socket.html?highlight=socket#socket.SOCK_DGRAM)

`tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`

**TCP服务端和客户端示例**

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

**执行 TCP 服务端和客户端**

服务端输出如下：

```
waiting for connection...
...connected from: ('127.0.0.1', 57223)
```

客户端输入及输出如下：

```
> hi
[Mon May  7 20:05:26 2018] hi
> spanish
[Mon May  7 20:05:33 2018] spanish
> 
```

#### [`socketserver`](https://docs.python.org/3.6/library/socketserver.html?highlight=socketserver#module-socketserver) - 网络服务框架

**[Examples](https://docs.python.org/3.6/library/socketserver.html?highlight=socketserver#examples)**

#### [`asyncore`](https://docs.python.org/3.6/library/asyncore.html?highlight=asyncore#module-asyncore) / [`asynchat`](https://docs.python.org/3.6/library/asynchat.html#module-asynchat) - 异步 socket 处理器

#### [`select`](https://docs.python.org/3.6/library/select.html?highlight=select#module-select) / [`selectors`](https://docs.python.org/3.6/library/selectors.html#module-selectors)

> Note that on Windows, it only works for sockets;
>
> The [`selectors`](https://docs.python.org/3.6/library/selectors.html#module-selectors) module allows high-level and efficient I/O multiplexing, built upon the[`select`](https://docs.python.org/3.6/library/select.html?highlight=select#module-select) module primitives. Users are encouraged to use the [`selectors`](https://docs.python.org/3.6/library/selectors.html#module-selectors) module instead

### 因特网客户端编程

#### [`http`](https://docs.python.org/3.5/library/http.html#module-http) — HTTP 包

> Python3.0起，原 `httplib` 模块被并入 `http` 包中。

- [`http.client`](https://docs.python.org/3.5/library/http.client.html#module-http.client) 低级 HTTP 协议客户端; 高级 HTTP 协议客户端使用 [`urllib.request`](https://docs.python.org/3.5/library/urllib.request.html#module-urllib.request)
- [`http.server`](https://docs.python.org/3.5/library/http.server.html#module-http.server) 基于 [`socketserver`](https://docs.python.org/3.5/library/socketserver.html#module-socketserver) 的基础 HTTP 服务端类
- [`http.cookies`](https://docs.python.org/3.5/library/http.cookies.html#module-http.cookies) 使用cookie实施状态管理的实用程序
- [`http.cookiejar`](https://docs.python.org/3.5/library/http.cookiejar.html#module-http.cookiejar) 提供cookie的持久性

#### [`ftplib`](https://docs.python.org/3.6/library/ftplib.html?highlight=ftplib#module-ftplib) - FTP 协议客户端

```
>>> from ftplib import FTP
>>> ftp = FTP('ftp.debian.org')     # connect to host, default port
>>> ftp.login()                     # user anonymous, passwd anonymous@
'230 Login successful.'
>>> ftp.cwd('debian')               # change into "debian" directory
>>> ftp.retrlines('LIST')           # list directory contents
-rw-rw-r--    1 1176     1176         1063 Jun 15 10:18 README
...
drwxr-sr-x    5 1176     1176         4096 Dec 19  2000 pool
drwxr-sr-x    4 1176     1176         4096 Nov 17  2008 project
drwxr-xr-x    3 1176     1176         4096 Oct 10  2012 tools
'226 Directory send OK.'
>>> ftp.retrbinary('RETR README', open('README', 'wb').write)
'226 Transfer complete.'
>>> ftp.quit()
```
{% blockquote 主动和被动模式 https://zh.wikipedia.org/wiki/%E6%96%87%E4%BB%B6%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE#%E4%B8%BB%E5%8A%A8%E5%92%8C%E8%A2%AB%E5%8A%A8%E6%A8%A1%E5%BC%8F 文件传输协议 %}

主动模式要求客户端和服务器端同时打开并且监听一个端口以创建连接。在这种情况下，客户端由于安装了防火墙会产生一些问题。所以，创立了被动模式。被动模式只要求服务器端产生一个监听相应端口的进程，这样就可以绕过客户端安装了防火墙的问题。

{% endblockquote %}

> 从 Python2.1开始，默认为**被动模式**。

#### [`nntplib`](https://docs.python.org/3.6/library/nntplib.html?highlight=nntp#module-nntplib) - [网络新闻传输协议](https://zh.wikipedia.org/wiki/%E7%B6%B2%E8%B7%AF%E6%96%B0%E8%81%9E%E5%82%B3%E8%BC%B8%E5%8D%94%E5%AE%9A)

#### [`smtplib`](https://docs.python.org/3.6/library/smtplib.html?highlight=smtplib#module-smtplib) - SMTP 协议客户端

```
>>> from smtplib import SMTP
>>> with SMTP("domain.org") as smtp:
...     smtp.noop()
...
(250, b'Ok')
>>>
```

**[`SMTP Objects`](https://docs.python.org/3.6/library/smtplib.html?highlight=smtplib#smtp-objects)** [Example](https://docs.python.org/3.6/library/smtplib.html?highlight=smtplib#smtp-example)

```python
import smtplib

def prompt(prompt):
    return input(prompt).strip()

fromaddr = prompt("From: ")
toaddrs  = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message length is", len(msg))

server = smtplib.SMTP('localhost')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
```

#### [郵局協议（Post Office Protocol，简称 POP）](https://zh.wikipedia.org/wiki/%E9%83%B5%E5%B1%80%E5%8D%94%E5%AE%9A)

{% blockquote 邮局协议 https://zh.wikipedia.org/wiki/%E9%83%B5%E5%B1%80%E5%8D%94%E5%AE%9A %}

POP支持离线邮件处理。其具体过程是：邮件发送到服务器上，电子邮件客户端调用邮件客户机程序以连接服务器，并下载所有未阅读的电子邮件。这种离线访问模式是一种存储转发服务，将邮件从邮件服务器端送到个人终端机器上，一般是PC机或MAC。一旦邮件发送到PC机或MAC上，邮件服务器上的邮件将会被删除。但目前的POP3邮件服务器大都可以“只下载邮件，服务器端并不删除”，也就是改进的POP3协议。

{% endblockquote %}

##### [`poplib`](https://docs.python.org/3.6/library/poplib.html?highlight=poplib#module-poplib) - POP3 协议客户端

[`POP3 Objects`](https://docs.python.org/3.6/library/poplib.html?highlight=poplib#pop3-objects)

```python
import getpass, poplib

M = poplib.POP3('localhost')
M.user(getpass.getuser())
M.pass_(getpass.getpass())
numMessages = len(M.list()[1])
for i in range(numMessages):
    for j in M.retr(i+1)[1]:
        print(j)
```

#### [因特网信息访问协议（缩写为 IMAP，以前称作 交互邮件访问协议）](https://zh.wikipedia.org/wiki/%E5%9B%A0%E7%89%B9%E7%BD%91%E4%BF%A1%E6%81%AF%E8%AE%BF%E9%97%AE%E5%8D%8F%E8%AE%AE)

{% blockquote 因特网信息访问协议 https://zh.wikipedia.org/wiki/%E5%9B%A0%E7%89%B9%E7%BD%91%E4%BF%A1%E6%81%AF%E8%AE%BF%E9%97%AE%E5%8D%8F%E8%AE%AE %}

因特网信息访问协议（缩写为IMAP，以前称作交互邮件访问协议）是一个应用层协议，用来从本地邮件客户端（如Microsoft Outlook、Outlook Express、Foxmail、Mozilla Thunderbird）访问远程服务器上的邮件。

IMAP和POP3（Post Office Protocol - Version 3，邮局协议第三版）是邮件访问最为普遍的Internet标准协议。事实上所有现代的邮件客户端和服务器都对两者给予支持。IMAP现在的版本是“IMAP第四版第一次修订版”（IMAP4rev1），在 RFC 3501 中定义。

{% endblockquote %}

##### [`imaplib`](https://docs.python.org/3.6/library/imaplib.html#module-imaplib) — IMAP4 协议客户端

[`IMAP4 Objects`](https://docs.python.org/3.6/library/imaplib.html#imap4-objects)

```python
import getpass, imaplib

M = imaplib.IMAP4()
M.login(getpass.getuser(), getpass.getpass())
M.select()
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print('Message %s\n%s\n' % (num, data[0][1]))
M.close()
M.logout()
```

#### [`email`](https://docs.python.org/3.6/library/email.html?highlight=email#module-email) - An email and MIME handling package

#### [`smtpd`](https://docs.python.org/3.6/library/smtpd.html?highlight=smtpd#module-smtpd) - SMTP 服务端

#### [`base64`](https://docs.python.org/3.6/library/base64.html?highlight=base64#module-base64) - Base16, Base32, Base64, Base85 Data Encodings

#### [`mimetypes`](https://docs.python.org/3.6/library/mimetypes.html?highlight=mimetypes#module-mimetypes) - Map filenames to MIME types

{% blockquote 互联网媒体类型 https://zh.wikipedia.org/wiki/%E4%BA%92%E8%81%94%E7%BD%91%E5%AA%92%E4%BD%93%E7%B1%BB%E5%9E%8B %}

互联网媒体类型（Internet media type，也称为MIME类型（MIME type）或内容类型（content type））是给互联网上传输的内容赋予的分类类型。一份内容的互联网媒体类型是由其文件格式与内容决定的。互联网媒体类型与文件拓展名相对应，因此计算机系统常常通过拓展名来确定一个文件的媒体类型并决定与其相关联的软件。互联网媒体类型的分类标准由互联网号码分配局（IANA）发布。1996年十一月，媒体类型在RFC 2045中被最初定义，当时仅被使用在SMTP协议的电子邮件中。现在其他的协议（比如HTTP或者SIP）也都常使用MIME类型。 一个MIME类型至少包括两个部分：一个类型（type）和一个子类型（subtype）。此外，它还可能包括一个或多个可选参数（optional parameter）。比如，HTML文件的互联网媒体类型可能是

text/html; charset = UTF-8

在这个例子中，文件类型为text，子类型为html，而charset是一个可选参数，其值为UTF-8。

{% endblockquote %}

#### [`binascii`](https://docs.python.org/3.6/library/binascii.html?highlight=binascii#module-binascii) - Convert between binary and ASCII

#### [`binhex`](https://docs.python.org/3.6/library/binhex.html?highlight=binhex#module-binhex) - Encode and decode binhex4 files

#### [`quopri`](https://docs.python.org/3.6/library/quopri.html#module-quopri) - Encode and decode MIME quoted-printable data

### 多线程编程

#### [`_thread`](https://docs.python.org/3.6/library/_thread.html#module-_thread) - 低级线程 API

#### [`threading`](https://docs.python.org/3.6/library/threading.html#module-threading) - 基于 `_thread` 的高级线程接口

> `threading`模块支持守护线程([`daemon`](https://docs.python.org/3.6/library/threading.html?highlight=daemon#threading.Thread.daemon) thread)，其工作方式是：守护线程一般是一个等待客户端请求服务的服务器。如果没有客户端请求，守护线程就是空闲的。如果把一个线程设置为守护线程，就表示这个线程是**不重要的**，进程退出时不需要等待这个线程执行完成。
>
> 如果主线程准备退出时，不需要等待某些子线程完成，就可以为这些子线程设置守护线程标记。

##### 创建 Thread 实例，传给它一个函数

```python
import threading
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = list(range(len(loops)))

    for i in nloops:
        t = threading.Thread(target=loop,
                             args=(i, loops[i]))
        threads.append(t)

    for i in nloops:  # start threads
        threads[i].start()

    for i in nloops:  # wait for all
        threads[i].join()  # threads to finish

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
```

当所有线程都被分配完毕后，通过调用每个线程的 `start()` 方法让它们开始执行，而不是在这之前就会执行。

`join()` 方法将等待线程结束，或者在提供了超时时间的情况下，达到超时时间。一旦线程启动，它们就会一直执行，知道给定的函数完成之后退出。如果主线程还有其他事情要做，而不是等待某些线程完成，就可以不调用 `join()` 。 `join()` 方法只有在需要等待线程完成的时候才是有用的。



