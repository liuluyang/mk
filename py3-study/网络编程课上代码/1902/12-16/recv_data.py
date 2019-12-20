# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/17 8:51


def recv_data(conn, data_size, bufsize=1024 * 8):
    """
    接收数据
    :param conn:
    :param data_size:
    :return:
    """
    while data_size:
        bufsize = bufsize if data_size >= bufsize else data_size
        d = conn.recv(bufsize)
        if not d:
            break
        data_size -= len(d)

        yield d