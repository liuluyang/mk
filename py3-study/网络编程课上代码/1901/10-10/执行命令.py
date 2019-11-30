# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/10 10:31


import subprocess
import os
# print(os.path.dirname(__file__))
# 第一个参数是执行的命令
res = subprocess.Popen('ipconfig', shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                       cwd=os.path.dirname(__file__)           # 执行命令时，所在系统路径，如果不填默认当前路径
                       )
print(res.stderr.read().decode('GBK'), 1111)   # 错误信息读取
print(res.stdout.read().decode('GBK'), 2222)   # 正确信息读取
