import sys
import os
"""
方法一：
把当前路径加入环境变量
"""
# sys.path.append(os.path.dirname(__file__))

import world
"""
方法二：
项目根路径导入
"""
# from mkdir_demo import world



world.w()

def h():
    print('this is hello module')