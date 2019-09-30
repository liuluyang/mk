from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait
import time

"""
线程池
"""

def task(num):

    r = num * 2
    print(r)
    time.sleep(1)
    return r


pool = ThreadPoolExecutor(max_workers=3)
p_list = []
for i in range(5):
    p = pool.submit(task, i)   # 提交执行任务
    p_list.append(p)

# pool.shutdown()              # 相当于进程池的pool.close()+pool.join()操作
# for p in p_list:
#     print(p.result())        # 获取任务执行结果


# print(p_list)
print('end')