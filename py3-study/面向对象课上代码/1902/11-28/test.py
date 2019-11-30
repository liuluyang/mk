# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/11/28 13:17



import uuid
import time

uid_set = set()
for i in range(100):
    uid  = str(uuid.uuid1())
    print(time.time())
    print(uid)
    uid_set.add(uid.split('-')[3])

print(len(uid_set), uid_set)