from graphics import *
from collections import deque
from edge import Edge


class Bot():
    def __init__(self, startNode,window, command):
        self.curNode = startNode
        self.x = self.curNode.x
        self.y = self.curNode.y
        self.instructor = command

        self.win = window
        self.edgeQue = deque()
        self.speed = 4
        self.curPosition = startNode.pos
        self.completion = 0
        self.curEdge = None
        self.curImage = Image(Point(self.x,self.y), "img/bot.png").draw(self.win)
        self.request = None
        self.idle = False

    def setPath(self,path):
        self.edgeQue = path
    def move(self):
        
        if self.curEdge is None:
            if len(self.edgeQue) > 0:                
                self.curEdge = self.edgeQue.popleft()
            else:
                out = self.instructor.giveRequest()
                if out is not None:
                    self.edgeQue = out[0]
                    self.request = out[1]
                    self.idle = False
                else:
                    self.idle = True

            return
        
        tempPos,self.completion = self.curEdge.sendCurrentLocation(self.speed, self.completion)
        if self.completion > 1:
            self.curNode = self.curEdge.end
            if (self.request is not None) and self.curNode is self.request.goalNode:
                self.request.endRequest()
                self.request = None

            self.x = self.curNode.x
            self.y = self.curNode.y
            self.completion = 0
            self.curEdge = None
        else:
            self.x = tempPos[0]
            self.y = tempPos[1]
        

    def draw(self):
        if(not self.idle):
            self.curImage.undraw()
            self.curImage = Image(Point(self.x,self.y), "img/bot.png").draw(self.win)
            """self.curImage = Circle(Point(self.x,self.y),8)
            self.curImage.setFill(color_rgb(0,168,168))
            self.curImage.draw(self.win)"""

        
        




    

