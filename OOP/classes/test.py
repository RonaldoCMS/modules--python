class Test:
    def __init__(self, x):
        super().__init__()
        self.x = x


t = Test(2)
print(t.x)
del t
