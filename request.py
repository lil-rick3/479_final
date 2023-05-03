from graphics import *
class Request():
    def __init__(self, goal, node_dict, window):
        # loc is an int refering to the node
        self.loc = goal
        self.goalNode = node_dict[goal]
        self.bot = None
        self.win = window
        self.endImage = Image(Point(self.goalNode.x,self.goalNode.y), "img/customer.png").draw(self.win)
    def endRequest(self):
        self.endImage.undraw()
        
    
