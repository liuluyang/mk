from wsgiref.simple_server import make_server


def application(environ, start_response):
    for k in environ.keys():
        print(k)
    start_response('200 OK', [('Content-Type', 'text/html')])

    return [b"<h1>hello world</h1>", b'123']


if __name__ == '__main__':
    app = make_server('', 9001, application)
    print('start ...')
    app.serve_forever()