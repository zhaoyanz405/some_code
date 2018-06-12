class SingleTon(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(SingleTon, cls).__new__(cls, *args, **kw)
        return cls._instance

class ForTest(SingleTon):
    """docstring for ForTest."""
    def __init__(self):
        super(ForTest, self).__init__()
        self.arg = 1

a = ForTest()
b = ForTest()

print(id(a))
print(id(b))
