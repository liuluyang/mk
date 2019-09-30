

##################################################### 继承、派生 ######################

class List(list): #继承list所有的属性，也可以派生出自己新的，比如append和mid
    def append(self, p_object):
        ' 派生自己的append：加上类型检查'
        if not isinstance(p_object,int):
            raise TypeError('must be int')
        super().append(p_object)
        # self.append(p_object)            # 注意：此方法会出现循环调用，导致异常

    @property
    def mid(self):
        '新增自己的属性'
        index=len(self)//2
        return self[index]

# lst = List([2])
# lst.append(1)
# print(lst)
# print(lst.mid)


#################################################  授权01 ######################
#授权：授权是包装的一个特性, 包装一个类型通常是对已存在的类型的一些定制,这种做法可以新建,修改或删除原有产品的功能。其它的则保持原样。
# 授权的过程,即是所有更新的功能都是由新类的某部分来处理,但已存在的功能就授权给对象的默认属性。
# 实现授权的关键点就是覆盖 __getattr__ 方法

import time
class FileHandle01:

    def __init__(self,filename,mode='r',encoding='utf-8'):
        self.file=open(filename,mode,encoding=encoding)

    def write(self,line):
        t=time.strftime('%Y-%m-%d %T')
        self.file.write('%s %s' %(t,line))

    def __getattr__(self, item):
        return getattr(self.file,item)

# f1=FileHandle01('b.txt','a+')
# f1.write('你好哇，李银河。\n')
# f1.seek(0)
# print(f1.read())
# f1.close()


##################################################  授权02 ######################

class FileHandle02:

    def __init__(self,filename,mode='r',encoding='utf-8'):
        if 'b' in mode:
            self.file=open(filename,mode)
        else:
            self.file=open(filename,mode,encoding=encoding)
        self.filename=filename
        self.mode=mode
        self.encoding=encoding

    def write(self,line):
        if 'b' in self.mode:
            if not isinstance(line,bytes):
                line = line.encode(encoding=self.encoding)
        self.file.write(line)

    # 必须实现这个方法，不然文件其它功能无法实现
    def __getattr__(self, item):
        return getattr(self.file,item)

    def __str__(self):
        if 'b' in self.mode:
            res="<_io.BufferedReader name='%s'>" %self.filename
        else:
            res="<_io.TextIOWrapper name='%s' mode='%s' encoding='%s'>" %(self.filename,self.mode,self.encoding)
        return res

# f1=FileHandle02('b.txt','wb')
# f1.write('你好啊啊啊啊啊')
# f1.write('你好啊'.encode('utf-8'))
# print(f1)
# f1.close()