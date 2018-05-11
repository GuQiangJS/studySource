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

[`socket.sendall(*bytes*[, *flags*])`](https://docs.python.org/3/library/socket.html?highlight=getservbyname#socket.socket.sendall) 与 [`socket.send(*bytes*[, *flags*])`](https://docs.python.org/3/library/socket.html?highlight=getservbyname#socket.socket.send) 不同，此方法继续从字节发送数据，直到发送所有数据或发生错误。

[`socket.send(*bytes*[, *flags*])`](https://docs.python.org/3/library/socket.html?highlight=getservbyname#socket.socket.send) 返回发送的字节数。由应用程序负责检查所有数据是否已发送;

TCP服务端和客户端示例**

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

#### 练习

1. 实现`Python`库参考文档中关于`socket`模块中TCP客户端/服务端程序示例。令其可以识别以下命令。
   1. `date` 服务器将返回其当前日期/时间戳，即 `time.ctime()`
   2. `os` 获取操作系统信息（`os.name`）
   3. `ls` 列出当前目录文件清单（`os.listdir()`列出目录，`os.curdir`是当前目录）
2. `Daytime`服务。使用`socket.getservbyname()`来确定使用UDP协议的`daytime`服务的端口号。

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

##### 创建 Thread 实例，传给它一个函数（多线程模式1）

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

##### 创建 Thread 实例，传给它一个可调用的类的实例（多线程模式2）

```python
import threading
from time import sleep, ctime

loops = [4, 2]

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:        # create all threads
        t = threading.Thread(
            target=ThreadFunc(loop, (i, loops[i]),
            loop.__name__))
        threads.append(t)

    for i in nloops:        # start all threads
        threads[i].start()

    for i in nloops:        # wait for completion
        threads[i].join()

    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()
```

相对于上一个示例，本次主要是添加了`ThreadFunc`类，并在实例化`Thread`对象的同时实例化了可调用类`ThreadFunc`。

当创建新线程时，`Thread`类的代码将调用`ThreadFunc`对象，对此会调用`__call__()`这个特殊方法。

##### 派生 [Thread](https://docs.python.org/3/library/threading.html?highlight=threading%20thread#thread-objects) 的子类，并创建子类的实例（多线程模式3 - 推荐方式）

```python
import threading
from time import sleep, ctime

loops = [4, 2]

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self, name=name)
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]),
            loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()
```

> 对于多线程来说，相对推荐这个模式，只需要创建 [`Thread`](https://docs.python.org/3/library/threading.html?highlight=threading%20thread#threading.Thread) 的派生类，并重写 `__init__()` 及 [`run()`](https://docs.python.org/3/library/threading.html?highlight=threading%20thread#threading.Thread.run) 方法即可

#### 多线程实践

##### 图书排名示例

```python
import urllib.request
from atexit import register
from re import compile
from threading import Thread
from time import ctime

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'https://www.amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}


def getRanking(isbn):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')]
    o = opener.open('{0}{1}'.format(AMZN, isbn))
    data = str(o.read(), 'utf-8')
    opener.close()
    return REGEX.findall(data)[0]


def _showRanking(isbn):
    print('- %r ranked %s' % (
        ISBNs[isbn], getRanking(isbn)))


def _main():
    print('At', ctime(), 'on Amazon...')
    for isbn in ISBNs:
        Thread(target=_showRanking, args=(isbn,)).start()  # _showRanking(isbn)


@register
def _atexit():
    print('all DONE at:', ctime())


if __name__ == '__main__':
    _main()
```

{% blockquote 竞争冒险 https://zh.wikipedia.org/wiki/%E7%AB%B6%E7%88%AD%E5%8D%B1%E5%AE%B3 %}

**竞争冒险**（race hazard）又名**竞态条件**、**竞争条件**（race condition），它旨在描述一个系统或者进程的输出依赖于不受控制的事件出现顺序或者出现时机。此词源自于两个信号试着彼此竞争，来影响谁先输出。

举例来说，如果计算机中的两个[进程](https://zh.wikipedia.org/wiki/%E8%BF%9B%E7%A8%8B)同时试图修改一个共享内存的内容，在没有[并发控制](https://zh.wikipedia.org/wiki/%E5%B9%B6%E5%8F%91%E6%8E%A7%E5%88%B6)的情况下，最后的结果依赖于两个进程的执行顺序与时机。而且如果发生了并发访问冲突，则最后的结果是不正确的。

竞争冒险常见于不良设计的电子系统，尤其是逻辑电路。但它们在[软件](https://zh.wikipedia.org/wiki/%E8%BB%9F%E9%AB%94)中也比较常见，尤其是有采用[多线程](https://zh.wikipedia.org/wiki/%E5%A4%9A%E7%BA%BF%E7%A8%8B)技术的软件。

{% endblockquote %}

##### [Lock Objects](https://docs.python.org/3/library/threading.html?highlight=threading#lock-objects)

**原始锁定是一种同步原语，在锁定时不属于特定线程**。

**当多个线程在[`acquire()`](https://docs.python.org/3/library/threading.html?highlight=threading#threading.Lock.acquire)等待状态转为解锁状态时被阻塞时，当一个[`release()`](https://docs.python.org/3/library/threading.html?highlight=threading#threading.Lock.release) 呼叫将状态重置为解锁状态时，只有一个线程继续进行; 哪一个等待的线程没有被定义，并且可能会因实现而有所不同。**

```python
#!/usr/bin/env python

from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    print('[%s] Started %s' % (ctime(), myname)) #print '[{0}] Started {1}'.format(ctime(), myname)
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('[%s] Completed %s (%d secs)' % ( #print '[{0}] Completed {1} ({2} secs)'.format(
        ctime(), myname, nsec))
    print('    (remaining: %s)' % (remaining or 'NONE')) #print '    (remaining: {0})'.format(remaining or 'NONE')
    lock.release()

def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()
```

```
[Thu May 10 15:52:48 2018] Started Thread-1
[Thu May 10 15:52:48 2018] Started Thread-2
[Thu May 10 15:52:48 2018] Started Thread-3
[Thu May 10 15:52:48 2018] Started Thread-4
[Thu May 10 15:52:51 2018] Completed Thread-4 (3 secs)
    (remaining: Thread-1, Thread-3, Thread-2)
[Thu May 10 15:52:51 2018] Completed Thread-2 (3 secs)
    (remaining: Thread-1, Thread-3)
[Thu May 10 15:52:52 2018] Completed Thread-1 (4 secs)
    (remaining: Thread-3)
[Thu May 10 15:52:52 2018] Completed Thread-3 (4 secs)
    (remaining: NONE)
all DONE at: Thu May 10 15:52:52 2018
```

以上示例中由于 `sleep(nsec)` 的存在，才造成了输出后半部分不同线程的结束顺序不同。

> 个人理解：Lock锁线程后会造成所有线程的阻塞和等待。

##### 上下文管理器 [with](https://docs.python.org/3/library/threading.html?highlight=threading#using-locks-conditions-and-semaphores-in-the-with-statement)

```python
with some_lock:
    # do something...
```

与以下代码是等价的

```python
some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()
```

#### 信号量([Semaphore Objects](https://docs.python.org/3/library/threading.html?highlight=threading#semaphore-objects))

一个信号量管理一个内部计数器，该计数器由每个 [`release()`](https://docs.python.org/3/library/threading.html?highlight=threading#threading.Semaphore.release)调用递减，并由每个[`release()`](https://docs.python.org/3/library/threading.html?highlight=threading#threading.Semaphore.release)调用递增。 柜台不能低于零; 当 [`release()`](https://docs.python.org/3/library/threading.html?highlight=threading#threading.Semaphore.release)发现它为零时，它会阻塞，等待其他线程调用[`release()`](https://docs.python.org/3/library/threading.html?highlight=threading#threading.Semaphore.release)。

> 信号量通常用于保护容量有限的资源。如果资源的大小是固定的，就应该使用有界的信号量。

主线程中定义信号量

```python
maxconnections = 5
# ...
pool_sema = BoundedSemaphore(value=maxconnections)
```

工作线程在需要连接到服务器时调用信号量的获取和释放方法：

```python
with pool_sema:
    conn = connectdb()
    try:
        # ... use connection ...
    finally:
        conn.close()
```

```python
import random
import time
from atexit import register
from threading import Thread, currentThread, BoundedSemaphore

MAX = 2
_sem = BoundedSemaphore(MAX)


def op(index):
    with _sem:
        threadName = currentThread().name
        print('{1} thread {0} 开始执行.'.format(threadName, time.ctime()))
        sec = random.randint(1, 10)
        time.sleep(sec)
        print('{1} thread {0} 开始完成.'.format(threadName, time.ctime()))


@register
def _atexit():
    print('all DONE')


def _main():
    for i in range(5):
        Thread(target=op, args=(str(i),)).start()


if __name__ == '__main__':
    _main()
```

输出内容如下：

```
Thu May 10 16:14:10 2018 thread Thread-1 开始执行.
Thu May 10 16:14:10 2018 thread Thread-2 开始执行.
Thu May 10 16:14:15 2018 thread Thread-1 开始完成.
Thu May 10 16:14:15 2018 thread Thread-3 开始执行.
Thu May 10 16:14:20 2018 thread Thread-2 开始完成.
Thu May 10 16:14:20 2018 thread Thread-4 开始执行.
Thu May 10 16:14:21 2018 thread Thread-3 开始完成.
Thu May 10 16:14:21 2018 thread Thread-5 开始执行.
Thu May 10 16:14:28 2018 thread Thread-5 开始完成.
Thu May 10 16:14:29 2018 thread Thread-4 开始完成.
all DONE
```

可以看到，开始执行时，最多只执行了 2 个线程，其他线程都在等待。当某一线程执行完成后，剩余线程中的一条开始执行。

#### 同步队列 - [`queue`](https://docs.python.org/3/library/queue.html?highlight=queue#module-queue) — A synchronized queue class

在多线程之间进行数据交换的利器。

[`queue.Queue(*maxsize=0*)`](https://docs.python.org/3/library/queue.html?highlight=queue#queue.Queue) 创建一个**先入先出**的队列。

[`queue.LifoQueue(maxsize=0)`]() 创建一个**后入先出**的队列。

[`queue.PriorityQueue(maxsize=0)`](https://docs.python.org/3/library/queue.html?highlight=queue#queue.PriorityQueue) 创建一个[**优先队列**](https://zh.wikipedia.org/wiki/%E5%84%AA%E5%85%88%E4%BD%87%E5%88%97)。

> `maxsize`是一个整数，用于设置可以放入队列中的项目数的上限。一旦达到此大小，插入将会阻塞，直到消耗队列项目。如果`maxsize`小于或等于零，则队列大小是无限的。

#### 多进程

由于 Python 的 GIL 的限制，多线程更适合于 I/O 密集型应用（I/O释放了GIL，可以允许更多的并发），而不是计算密集型应用。对于计算密集型应用，为了实现更好的并行性，需要使用**多进程**，以便让CPU的其他内核来执行。

##### [`subprocess`](https://docs.python.org/3/library/subprocess.html?highlight=subprocess#module-subprocess) - 子进程管理

##### [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html?highlight=multiprocess#module-multiprocessing) - 并行进程，该模块允许程序员充分利用给定机器上的多个处理器。

##### [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html?highlight=concurrent%20futures#module-concurrent.futures) - 启动并行任务

Python 3.2 开始提供的一个高级库。可以让开发者不在过分关注同步和线程/进程的管理。

只需要指定线程池/进程池的最大工作数量，提交任务，然后整理结果即可。

###### [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html?highlight=concurrent%20futures#concurrent.futures.ThreadPoolExecutor) - 支持异步调用的线程池

```python
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
```

###### [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html?highlight=concurrent%20futures#concurrent.futures.ProcessPoolExecutor) - 支持异步调用的进程池

```python
import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()
```

#### 练习

1. 线程和文件。

   1. 创建一个函数，给出一个字节值和一个文件名，然后显示文件中该字节出现的次数。
   2. 假设输入的文件非常大。该文件允许有多个读者，现在请修改你的解决方案，创建多个线程，使每个线程负责文件某一部分的计数。然后将每个线程的数据进行整合，提供正确的总数。使用 `timeit` 模块对单线程和多线程方案进行计时。

   EXP：对于此类问题，由于并不是I/O密集型操作（单一文本只读取一次的情况下）。由于多线程需要对文本进行分拆，并且多线程之间的锁定和解锁操作等多余操作，会造成采用多线程的性能会低于单一线程性能。

2. 线程、文件和正则表达式。有一个非常大的邮件文件；如果没有（把所有的邮件合并到一个文本文件中）。任务是，使用正则表达式用于识别email地址和web站点的URL。并将其转换为链接形式保存到.html新文件中，当时用Web浏览器打开该文件时，这些链接应该是可以单击的。使用线程对这个大文本文件的转换过程进行分割，最后整合所有结果到一个新的.html文件中。