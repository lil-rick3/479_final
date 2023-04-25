from graphics import *
class Request():
    def __init__(self, goal, node_dict, window):
        self.loc = goal
        self.goalNode = node_dict[goal]
        self.bot = None
        self.win = window
        self.endimag = Image(Point(self.goalNode.x,self.goalNode.y), "img/customer.png").draw(self.win)
        
    
