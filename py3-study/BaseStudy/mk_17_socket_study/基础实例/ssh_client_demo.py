import socket

ip_port = ('127.0.0.1', 8080)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = s.connect_ex(ip_port)

while True:
    msg = input('>>: ').strip()
    if len(msg) == 0: continue
    if msg == 'quit': break

    s.send(msg.encode('utf-8'))
    print(s.recv(1024).decode('GBK'))

    # result = b''
    # while True:
    #     act_res = s.recv(1024)
    #     result += act_res
    #     if len(act_res) < 1024:
    #         break
    # print(result.decode('GBK'))