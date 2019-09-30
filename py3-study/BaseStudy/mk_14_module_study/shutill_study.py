import shutil
import zipfile, tarfile
import os

"""
shutil模块学习
"""

"""
复制文件
"""
# shutil.copyfile('comments.txt', 'copy.txt')

"""
压缩指定目录下所有文件
base_name 压缩包的文件名，也可以是压缩包的路径；只是文件名时，则保存至当前目录下，否则保存至指定路径；
format：压缩包种类，“zip”, “tar”, “bztar”，“gztar”；
base_dir：指定要压缩文件的路径，可以指定路径下的文件名，也可以指定路径；
root_dir：指定要压缩的路径根目录（默认当前目录），只能指定路径，优先级低于base_dir；

注意：
如果base_name 在base_dir或root_dir里面
此操作会出现递归拷贝压缩导致文件损坏
"""
base_path = os.path.abspath('.')
print(base_path)
# os.path.join(base_path, 'mkdir_demo')
shutil.make_archive(base_name='../压缩', format='zip', root_dir=os.path.join(base_path, 'mkdir_demo'))

"""
zip压缩、解压文件
"""
# r = zipfile.ZipFile('test_zip.zip', 'w')
# r.write('comments.txt')   # 无法压缩文件夹
# r.write('copy.txt')
# r.close()

# r2 = zipfile.ZipFile('test_zip.zip', 'r')
# r2.extractall(r'unzip')  # 指定解压目录，如果目录不存在会进行创建
# r2.close()

"""
tar压缩、解压文件
"""
# r = tarfile.TarFile('test_tar.tar', 'w')
# r.add('images')            # 可以压缩文件夹
# r.close()


"""
学习目标：批量化自动压缩解压
"""

