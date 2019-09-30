# !/uer/bin/env python
# _*_ utf-8 _*_
# __author__ = Miller
#  2019/9/27 9:46

import os
import subprocess

path = os.path.dirname(__file__)
print(path)
while True:

    cmd = input('>>>')
    if cmd.startswith('cd'):
        cmd += ' & dir'

    res = subprocess.Popen(cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                           cwd=path
                           )

    out = res.stdout.read().decode('GBK')
    err = res.stderr.read().decode('GBK')
    print(out)
    print(err)
    if cmd.startswith('cd') and out:
        path = out.split('\r\n')[3].split()[0]
        # print('_____________________', path)

# import os
#
# # 第一个参数是执行的命令
# res = subprocess.Popen('dir', shell=True,
#                                stdout=subprocess.PIPE,
#                                stdin=subprocess.PIPE,
#                                stderr=subprocess.PIPE,
#                        cwd=os.path.dirname(__file__)           # 执行命令时，所在系统路径，如果不填默认当前路径
#                        )
# print(res.stderr.read().decode('GBK'))   # 错误信息读取
# print(res.stdout.read().decode('GBK'))   # 正确信息读取
