from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16209183'
API_KEY = 'DnB2038Qr4H9EzFffOiuHvY9'
SECRET_KEY = 'KFhQ01HO52NihPA41tiIsqxcwlNuR3l6'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def code_get():
    image = get_file_content('images/wenzi_02.jpg')

    """ 调用通用文字识别, 图片参数为本地图片 """
    # code = client.basicGeneral(image)
    # print(code)

    """通用文字识别 高精度版"""
    # code = client.basicAccurate(image)
    # print(code)

    """ 如果有可选参数 """
    # options = {}
    # options["language_type"] = "CHN_ENG"
    # options["detect_direction"] = "true"
    # options["detect_language"] = "true"
    # options["probability"] = "true"

    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    # code = client.basicGeneral(image, options)
    # print(code)

    url = "http//www.x.com/sample.jpg"

    """ 调用通用文字识别, 图片参数为远程url图片 """
    # client.basicGeneralUrl(url)

    """ 如果有可选参数 """
    # options = {}
    # options["language_type"] = "CHN_ENG"
    # options["detect_direction"] = "true"
    # options["detect_language"] = "true"
    # options["probability"] = "true"

    """ 带参数调用通用文字识别, 图片参数为远程url图片 """
    # client.basicGeneralUrl(url, options)


if __name__ == '__main__':
    # code_get()
    pass