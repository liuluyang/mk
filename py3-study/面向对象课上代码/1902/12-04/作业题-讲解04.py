



class Context:

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def do_something(self):

        print('做点事情。。。')
        pass


with Context() as ctx:
    ctx.do_something()