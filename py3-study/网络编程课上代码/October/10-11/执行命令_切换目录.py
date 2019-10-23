# !/uer/bin/env python
# _*_ utf-8 _*_
# __author__ = Miller
#  2019/9/27 9:46

import os
import subprocess

path = os.path.dirname(os.path.abspath(__file__))
# print(path)
while True:
    cmd = input('>>>')
    if cmd.startswith('cd'):
        cmd += ' & dir'

    res = subprocess.Popen(cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                           cwd=os.getcwd()
                           )

    out = res.stdout.read().decode('GBK')
    err = res.stderr.read().decode('GBK')
    print(out)
    print(err)
    if cmd.startswith('cd') and out:
        path = out.split('\r\n')[3].split()[0]
        os.chdir(path)
