

class Obj():
    X = 0

    def __init__(self, Y):
        self.Y = Y


a = Obj(2)
b = Obj(3)

Obj.X = 5

print("a.X:\t", a.X, "\ta.Y:\t", a.Y)
print("b.X:\t", b.X, "\tb.Y:\t", b.Y)

Obj.X = 7

print("a.X:\t", a.X, "\ta.Y:\t", a.Y)
print("b.X:\t", b.X, "\tb.Y:\t", b.Y)
