# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/9 11:44



err = 'e'
out = 'hello'

data, status = (err, 'error') if err else (out, 'ok')

print(data, status)