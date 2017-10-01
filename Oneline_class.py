class test: __init__, add = lambda self: [setattr(self,'x',123),setattr(self,'y',456),None][-1], lambda self:self.x + self.y
x = test()
print(x.add())
