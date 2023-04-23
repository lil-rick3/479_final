from graphics import *
from collections import deque
from edge import Edge


class Bot():
    def __init__(self, startNode,window, edge_dict):
        self.curNode = startNode
        self.x = self.curNode.x
        self.y = self.curNode.y
        

        self.win = window
        self.edgeQue = deque([edge_dict["2,4"], edge_dict["4,26"], edge_dict["26,10"],edge_dict["10,21"],edge_dict["21,20"]])
        self.speed = 4
        self.curPosition = startNode.pos
        self.completion = 0
        self.curEdge = None
        self.curImage = None

    def move(self):
        self.curImage.undraw()
        if self.curEdge is None:
            if len(self.edgeQue) > 0:                
                self.curEdge = self.edgeQue.popleft()
            else:
                return
        
        tempPos,self.completion = self.curEdge.sendCurrentLocation(self.speed, self.completion)
        if self.completion > 1:
            self.curNode = self.curEdge.end
            self.x = self.curNode.x
            self.y = self.curNode.y
            self.completion = 0
            self.curEdge = None
        else:
            self.x = tempPos[0]
            self.y = tempPos[1]
        

    def draw(self):
        self.curImage = Image(Point(self.x,self.y), "img/bot.png").draw(self.win)

        
        




    

