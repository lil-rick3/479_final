from graphics import*
class Node():
    def __init__(self, xPos, yPos, window, id):
        self.x = xPos
        self.y = yPos
        self.pos = Point(self.x, self.y)
        self.edges = {}
        self.nodesOut = {}
        self.win = window
        self.id = id
        self.c = Circle(self.pos, 10)
        self.c.setFill(color_rgb(200,0,0))
        self.name = Text(Point(self.x - 20, self.y), str(self.id))
        self.name.setTextColor(color_rgb(250, 243, 40))


    def draw(self):
        self.c.draw(self.win)
        self.name.draw(self.win)