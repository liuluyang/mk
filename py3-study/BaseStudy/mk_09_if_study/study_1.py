

"""
流程控制
"""
"""
之前的学习代码都是依次由上至下的执行，
如果想做一些复杂的控制就需要用到判断语句，
来决定运行那些代码
"""

"""
但分支
"""
# age = int(input('请输入年龄：'))  #注意类型转换
# if age < 18:          #注意语法冒号:
#     print('未满18岁') #注意语法缩进

"""
双分支
"""
# age = int(input('请输入年龄：'))
# if age < 18:
#     print('未满18岁')
# else:
#     print('已满18岁')

"""
多分支
依次判断，符合一个条件之后，不会再去判断其他条件
"""
# num = 10
# my_num = int(input('输入数字：'))
#
# if my_num > num:
#     print('大于%d'%(num))
# elif my_num < num:
#     print('小于%s'%(num))
# else:
#     print('等于%s'%(num))
#
# print('结束')