# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/12 9:28



import subprocess
import os
import re


def execut_cmd(cmd):

    cmd = cmd.strip()
    if cmd.startswith('cd'):
        cmd += ' &dir'

    # 第一个参数是执行的命令
    res = subprocess.Popen(cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                           )

    out = res.stdout.read().decode('GBK')   # 正确信息读取
    err = res.stderr.read().decode('GBK')   # 错误信息读取

    if cmd.startswith('cd') and out:
        path = re.search('(.+)的目录', out)
        os.chdir(path.groups()[0].strip())

    return err if err else out

# print(execut_cmd('cd ..'))


