

import json


with open('info', 'w') as f:
    data = {'name':'xiaohei'}
    json.dump(data, f)


with open('info', 'r') as f:
    d = json.load(f)
    print(type(d), d)
