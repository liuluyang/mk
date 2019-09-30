import socket
import time
import json
import datetime

def index(client):
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf8"))
    client.send("<h1 style='color:red'>Hello, index</h1>".encode("utf8"))

def data(client):
    client.send("HTTP/1.1 200 OK\r\n\r\n".encode())
    client.send("<h1 style='color:red'>Hello, data</h1>".encode())

def time_now(client):
    client.send("HTTP/1.1 200 OK\r\n".encode())
    client.send("Token:11111111111\r\n\r\n".encode())
    client.send(("<h1 style='color:red'>%s</h1>"%(str(datetime.datetime.now()))).encode())

url_mapping = {
    '/': index,
    '/data': data,
    '/time':time_now
}

def handle_request(client):
    request_data = client.recv(1024).decode()
    if not request_data:
        return None

    print("请求信息: ")
    print(request_data)

    data = request_data.split('\r\n')
    print('处理之后：')
    print(data)

    path = data[0].split()[1]
    print('请求路径')
    print(path)

    func = url_mapping.get(path)
    if func:
        func(client)
    else:

        f = open('python之禅.txt', 'rb').read()
        print(len(f))
        f2 = open('pp.png', 'rb').read()
        print(len(f2))
        f3 = open('ms.pdf', 'rb').read()
        print(len(f3))
        # Content-Type: text/html; charset=utf-8
        # Content-Type: application/x-www-form-urlencoded
        # Content-Type: application/json
        client.send("HTTP/1.1 200 OK\r\n"
                    
                    # "Content-Disposition: attachment; filename=pp.png\r\n" # filename 控制文件名跟类型
                    # "Content-Type: image\png \r\n"

                    # 页面显示
                    # "Content-Type: text/html; charset=utf-8\r\n"
                    
                    #"Content-Disposition: attachment; filename=pp.png\r\n" # 必须头信息
                    #"Content-Length: 72334\r\n"
                    # "Content-Type: image\png \r\n\r\n".encode()                      # 必须头信息
                    
                    # 文件下载
                    # "Content-Disposition: attachment; filename=python之禅.txt\r\n" # 必须头信息
                    # "Content-Length: 765\r\n"
                    # "Content-Type: text/plain; charset=utf-8 \r\n"                      # 必须头信息
                    
                    # "Content-Disposition: attachment; filename=ms.pdf\r\n" # 必须头信息
                    # "Content-Type: application\pdf \r\n"

                    # "Content-Type: application/octet-stream\r\n"
                    
                    # "token: 111\r\n"
                    "Set-Cookie:f=1\r\n\r\n ".encode())

        # client.send("<h1 style='color:red'>网页找不到</h1>".encode())
        client.send(f3)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 8800))
    sock.listen(1)

    while True:
        print("the server is waiting for client-connection....")
        connection, address = sock.accept()
        try:
            handle_request(connection)
        except Exception as e:
            print('error:', e)
        connection.close()


if __name__ == '__main__':
    main()
