# Copyright (C) 2018 GuQiangJs.
# Licensed under https://www.gnu.org/licenses/gpl-3.0.html <see LICENSE file>

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
        # print('thread {0} 休眠 {1} 秒'.format(threadName,sec))
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
