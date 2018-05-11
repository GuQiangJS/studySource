# Copyright (C) 2018 GuQiangJs.
# Licensed under https://www.gnu.org/licenses/gpl-3.0.html <see LICENSE file>

import os
import random
import timeit
from threading import BoundedSemaphore,Thread
import queue

FILENAME='temp.txt'
SEARCH_CHAR=str(chr(random.randint(65,90))) # 待搜索的字符

_THREAD_COUNT = 10
_SEM = BoundedSemaphore(_THREAD_COUNT)

if not os.path.exists(FILENAME):
    with open(FILENAME,mode='wt+',encoding='utf-8') as f:
        for i in range(10*1024*1024):
            f.write(str(chr(random.randint(65,90))))


def __op(context,q,char=SEARCH_CHAR):
    q.put(context.count(char))

def mutliple():
    q = queue.Queue()
    lst=_CONTEXT.split(maxsplit=_THREAD_COUNT)
    ts=[]
    for l in lst:
        ts.append(Thread(target=__op, args=(l,q,SEARCH_CHAR)))
    for t in ts:
        t.start()
        t.join()
    c=0
    while not q.empty():
        i = q.get_nowait()
        c=c+i
    return c

_CONTEXT=''

with open(FILENAME,encoding='utf-8') as f:
    _CONTEXT=f.read()
    print('{0} count: {1} .'.format(SEARCH_CHAR,_CONTEXT.count(SEARCH_CHAR)))
    # print(timeit.timeit('[func("'+SEARCH_CHAR+'") for func in [single]]'))

    print('{0} count: {1} .'.format(SEARCH_CHAR,mutliple()))

    # print("Single Thread:"+str(timeit.timeit('r"{0}".count("{1}")'.format(_CONTEXT,SEARCH_CHAR), number=10)))
    # print(timeit.timeit("mutliple()", setup="import mutliple"))