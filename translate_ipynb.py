from __future__ import unicode_literals

import json
import logging
import os
import re
import sys
from bs4 import BeautifulSoup
from py_translator import Translator

dest = 'zh-cn'
encoding = 'utf-8'
fullpath = r''

replace_left = True
replace_right = True
replace_k = True
replace_l1 = True
replace_l2 = True
replace_shape = True
skip_math = True

RE_K = re.compile('(#+)[^ #]')
RE_MATH = re.compile('\$[^$]*\$')

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def trans(translator, str):
    if not translator:
        translator = newTranslator()
    math_dic = {}
    if skip_math:
        maths = RE_MATH.findall(str)
        if maths:
            for i in range(len(maths)):
                math_dic[maths[i]] = 'math_{0}_math'.format(i)
            for k, v in math_dic.items():
                str = str.replace(k, v)
    r = translator.translate(str, dest=dest).text
    if skip_math and math_dic:
        for k, v in math_dic.items():
            r = r.replace(v, ' ' + k + ' ')
    if replace_left:
        r = r.replace('（', '(')
    if replace_right:
        r = r.replace('）', ')')
    if replace_left:
        r = r.replace('“', '`')
    if replace_right:
        r = r.replace('”', '`')
    if replace_shape:
        r = r.replace('＃', '#')
    r = r.replace(r'\ text', r'\text')
    if replace_k:
        m = RE_K.search(r)
        if m:
            r = r.replace(m.group(1), m.group(1) + ' ')
    return '\n' + r


def newTranslator():
    return Translator(proxies={'http': '127.0.0.1:1087', 'https':
        '127.0.0.1:1087'})


def getInput():
    val = []
    while not val:
        s=input('input str:')
        while(s):
            empty_lines=0
            val.append(s)
            s=input()
            while(not s and empty_lines<5):
                s=input()
                empty_lines=empty_lines+1
    return val


if __name__ == '__main__':
    logging.info('自动转换英文到中文。可以设置跳过转换数学公式。\n\r')
    while True:
        str = getInput()
        if str:
            translator = newTranslator()
            for s in str:
                logging.info('\n\r' + trans(translator, s) + '\n\r')
