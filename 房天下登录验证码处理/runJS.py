# -*- coding: utf-8 -*-
# @Author  : 作者
# @Time    : 2024/4/9 13:45
# @Function:
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen,encoding='utf-8')
import execjs

class get_parames():
    def get_i(self):
        # 获取i参数
        with open('get_i.js', 'r', encoding='utf-8') as f:
            js_code = f.read()
        ctx = execjs.compile(js_code)
        return ctx.eval("get_i")

    def get_t(self,l):
        with open('get_t.js', 'r', encoding='utf-8') as f:
            js_code = f.read()
        ctx = execjs.compile(js_code)
        return ctx.call("main",l)


if __name__ == '__main__':
    get_parames = get_parames()


