import requests
import threading

def r(i):
    data = {
        'name':'liu',
        'pass':'111'
    }
    r= requests.post('http://127.0.0.1:8800/data{}'.format(i), data=data)
    print(r.status_code, r, r.text, r.json())

for i in range(1):
    t = threading.Thread(target=r, args=(i,))
    t.start()
