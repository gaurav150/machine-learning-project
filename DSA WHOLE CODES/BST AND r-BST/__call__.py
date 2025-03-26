# class Test():
#     def __init__(self):
#         pass
#     def __call__(self):
#         print("Invoking '__call__' method")

class Test():
    def __init__(self):
        pass
    def run(self):
        print("Invoking '__call__' method")
    __call__ = run

test = Test()
test()
test.run()
test.__call__()
test.__call__ = test.run