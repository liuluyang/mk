
import os

check_name = '10'

def check_file(path):

    file_list = os.listdir(path)

    for file_path in file_list:
        full_path = os.path.join(path, file_path)
        # if check_name in file_path:
        #     print(full_path)

        if os.path.isfile(full_path):
            print(full_path, '文件')
            pass
        else:
            print(full_path, '目录')
            pass
            check_file(full_path)



# check_file(r'F:\刘禄扬\project\project\education')

# for i in os.walk(r'F:\刘禄扬\project\project\education'):
#     print(i)