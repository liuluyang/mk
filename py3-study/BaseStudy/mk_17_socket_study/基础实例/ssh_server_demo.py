import socket
import subprocess

ip_port = ('127.0.0.1', 8080)
tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)

while True:
    conn, addr = tcp_socket_server.accept()
    print('客户端', addr)

    while True:
        cmd = conn.recv(1024)
        print("recv cmd", cmd)
        if len(cmd) == 0: break
        res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)

        stderr = res.stderr.read()
        stdout = res.stdout.read()
        if stderr:
            conn.send(stderr)
        else:
            conn.send(stdout)