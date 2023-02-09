class shape:
    area = 0
    def __init__(self):
        pass


class Square(shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        a = (self.length * self.length)
        print(a)

lenght = input()
s = Square(int(lenght))
s.area()