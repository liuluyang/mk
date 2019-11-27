
import time


def check_time(ischeck=True):

    def outer(func):

        def inner(*args, **kwargs):

            if ischeck:
                start_time = time.time()
                f = func(*args, **kwargs)
                print(time.time() - start_time)

                return f

            return func(*args, **kwargs)

        return inner

    return outer


@check_time(ischeck=False)
def add(n, m):

    return n + m


r = add(1, 2)
print(r)



