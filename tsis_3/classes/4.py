class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self):
        a = input()
        b = input()
        self.x += int(a)
        self.y += int(b)
        return self.x, self.y

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5


x1 = input()
y1 = input()
x2 = input()
y2 = input()
point1 = point(int(x1), int(y1))
point2 = point(int(x2), int(y2))
print(point1.dist(point2))
print(point1.move())
print(point1.show())