#to plot the points on a cartesian place which has 2 coordinates x and y. do teh following

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def move(self, a, b):
        self.x = a
        self.y = b
    
    def xmove(self, a):
        self.x = a

    def ymove(self, b):
        self.y = b

p1 = Point(4,5)
p1.reset()
print(p1.x,p1.y)
p1.move(5,6)
print(p1.x,p1.y)
p1.xmove(10)
print(p1.x,p1.y)
p1.ymove(9)
print(p1.x,p1.y)

