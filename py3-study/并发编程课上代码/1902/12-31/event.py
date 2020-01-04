# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/31 13:44


from threading import Event, Semaphore, Lock, RLock, Timer, Thread
import queue


event = Event()
print(event.isSet())
event.set()
print(event.wait())
print(event.clear())
print(event.isSet())