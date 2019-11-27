
import zipfile, tarfile, shutil


######################################## zipfile

def test_zip():

    # zip压缩文件
    r = zipfile.ZipFile('zip_test.zip', mode='w')
    r.write('test')
    r.write('json模块.py')
    # r.write('t')    # 不能压缩文件夹
    r.close()

# test_zip()

def test_unzip():

    # 解压文件
    r = zipfile.ZipFile('zip_test.zip', mode='r')
    r.extractall('../unzip_dir')    # 指定解压路径

# test_unzip()

############################################# tarfile


def test_tar():

    # tar压缩文件
    r = tarfile.TarFile('tar_test.tar', mode='w')
    r.add('test')
    r.add('json模块.py')
    r.add('t')
    r.close()

# test_tar()


def test_untar():

    # 解压文件
    r = tarfile.TarFile('tar_test.tar', mode='r')
    r.extractall('tarzip_dir')    # 指定解压路径

# test_untar()

############################################### shutil

# 复制文件
# shutil.copyfile('test', 'test_copy')

# 压缩
# 注意：压缩包不要放在被压缩的文件里面
# shutil.make_archive(base_name='../test_zip', format='zip', root_dir=r'E:\project\education\11-12')
















