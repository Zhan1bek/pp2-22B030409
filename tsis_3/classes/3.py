class shape:
    area = 0
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width



class rectangle(shape):
    def __init__(self, lenght, width):
        shape.__init__(self, lenght , width)

    def area(self):
        a = self.lenght * self.width
        print(a)

lenght = input()
width = input()
s = rectangle(int(lenght), int(width))
s.area()