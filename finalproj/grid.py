from graphics import *
class Grid():
    def __init__(self, width, height, separation,window):
        self.max_w = width
        self.max_h = height
        self.win = window
        self.separation = separation
        self.line_Arr = []
        self.text_Arr = []
        self.color = color_rgb(250, 243, 40)
        self.create_grid()
    
    def create_grid(self):
        x = 0
        while(x <= self.max_w):
            temp_line = Line(Point(x,0),Point(x, self.max_h))
            temp_text = Text(Point(x + 40, 20), str(x))
            temp_line.setFill(self.color)
            temp_text.setTextColor(self.color)
            self.text_Arr.append(temp_text)
            self.line_Arr.append(temp_line) 
            x += 100
        y = 0
        while(y <= self.max_h):
            temp_line = Line(Point(0,y),Point(self.max_w, y))
            temp_text = Text(Point(40, y +20), str(y))
            temp_line.setFill(self.color)
            temp_text.setTextColor(self.color)
            self.text_Arr.append(temp_text)
            self.line_Arr.append(temp_line) 
            y += 100
    def draw(self):
        for line in self.line_Arr:
            line.draw(self.win)
        for text in self.text_Arr:
            text.draw(self.win)
