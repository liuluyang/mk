

import time

###################################### 倒计时


def check_time():

    day_sec = 60*60*24
    hour_sec = 60*60
    min_sec = 60

    while True:
        timestamp_now = time.time()
        timestamp_last = time.mktime(time.strptime('2020-1-1 0:0:0', '%Y-%m-%d %H:%M:%S'))
        # print(timestamp_now, timestamp_last)
        period = timestamp_last - timestamp_now
        # print(period)

        day_nums, other = divmod(period, day_sec)
        # print(day_nums, other)

        hour_nums, other = divmod(other, hour_sec)
        # print(hour_nums, other)

        min_nums, other = divmod(other, min_sec)
        # print(min_nums, other)

        print('\r', '%s天 %s小时 %s分钟 %s秒'%(int(day_nums), int(hour_nums), int(min_nums), int(other)), end='')
        time.sleep(1)


# check_time()