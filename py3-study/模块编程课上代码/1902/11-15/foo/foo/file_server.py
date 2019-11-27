import os
import time
from datetime import timedelta
from flask import Flask, request, url_for, send_from_directory, redirect, render_template, send_file, make_response
from werkzeug.utils import secure_filename

# import sys
# # sys.path.append('E:/foo')
from docs.config import *


app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 1allowed_file_type024*1024
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
# images_path = os.path.join(os.getcwd(), 'images')

# dir_name = 'upload_file'
# common_dir_name = 'common_file'
# allowed_file_type = ['py', 'jpg', 'pdf', "png", 'zip', 'tar', 'rar', 'txt', 'docx']
# is_allowed_upload = True
# is_allowed_check = []
# is_allowed_download = []
# admin = '刘禄扬'
# password = '127.0.0.1'


def make_dir():
    date_now = time.strftime('%y-%m-%d', time.localtime())
    dir_name_now = '{}_{}'.format(dir_name, date_now)
    dir_full_path = os.path.join(os.getcwd(), dir_name_now)
    if not os.path.exists(dir_full_path):
        os.makedirs(dir_full_path)
    return dir_full_path


@app.route('/common/<filename>/<action>')
def common_file(filename, action):
    if action == 'look':
        as_attachment = False
    elif action == 'download':
        as_attachment = True
    else:
        return '未知操作！'
    return send_file(os.path.join(os.getcwd(), common_dir_name, filename), as_attachment=as_attachment)


@app.route('/common')   # 共文件查看接口
def common_file_index():
    static_path = os.path.join(os.getcwd(), common_dir_name)
    common_files = os.listdir(static_path)

    return render_template('common_file.html', common_files=common_files)


@app.route('/uploads/<filename>')
def upload_file(filename):
    if '*' in is_allowed_check or filename in is_allowed_check:
        return send_from_directory(make_dir(), filename)
    else:
        return '无权查看！'


@app.route('/downloads/<filename>')
def download_file(filename):
    if '*' in is_allowed_download or filename in is_allowed_download:
        return send_file(os.path.join(make_dir(), filename), as_attachment=True)
    else:
        return '无权下载！'


@app.route('/', methods=('GET', 'POST'))
def upload_index():
    static_path = make_dir()
    uploaded_files = os.listdir(static_path)
    if request.method == 'POST':
        real_ip = request.environ['REMOTE_ADDR']
        file = request.files['file']
        filename = file.filename
        file_type = filename.split('.')[-1]
        form = request.form.to_dict()
        name = form.get('name').strip()
        ip =  form.get('ip').strip()

        error = None
        if not filename:
            error = '未选择文件！'
        elif not name or ip != real_ip:
            error = '姓名为空或IP错误！'
        elif file_type not in allowed_file_type:
            error = '文件类型错误！'

        if not error:
            if is_allowed_upload or name==admin and ip==password:
                file.save(os.path.join(static_path, '{}.{}'.format(name, file_type)))
                return redirect(url_for('upload_index'))
            elif not is_allowed_upload:
                error = '上传通道已关闭！'
        return render_template('result_upload.html', error=error, uploaded_files=uploaded_files)
    return render_template('result_upload.html', uploaded_files=uploaded_files)
