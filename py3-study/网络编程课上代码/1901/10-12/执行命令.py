# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/10 10:31


import subprocess
import os
# print(os.path.dirname(__file__))
path = os.path.dirname(os.path.abspath(__file__))
print(path)
# 第一个参数是执行的命令
while True:
    cmd = input('请输入指令：')
    if cmd.startswith('cd'):
        cmd += ' & dir'

    res = subprocess.Popen(cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                    cwd=path           # 执行命令时，所在系统路径，如果不填默认当前路径
                           )

    print(res.stderr.read().decode('GBK'), 1111)   # 错误信息读取
    out = res.stdout.read().decode('GBK')          # 正确信息读取
    print(out)
    if cmd.startswith('cd') and out:
        path = out.split('\r\n')[3].split()[0]







