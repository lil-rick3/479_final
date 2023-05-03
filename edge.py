from node import Node
from graphics import *
import math

class Edge():
    
    def __init__(self, node1, node2, window,identity):
        self.start = node1
        self.id = identity
        self.start.edges[self.id] = self
        self.start.nodesOut[node2.id] = node2
        self.end = node2
        
        self.win = window
        self.thickness = 10

       
        self.makepath()
        self.distance = math.sqrt(pow(self.start.x - self.end.x,2) + pow(self.start.y - self.end.y,2))
        self.weight = self.distance

    def sendCurrentLocation(self, speed, completion):
        delta = speed/self.distance
        newPercentage = completion + delta
        x = int(newPercentage * (self.end.x - self.start.x) + self.start.x)
        y = int(newPercentage * (self.end.y - self.start.y) + self.start.y)
        newPoint = (x,y)
        return newPoint, newPercentage


    def makepath(self):
        
        try:
            dy = int(self.thickness * (-(self.end.x - self.start.x)/(self.end.y-self.start.y))/(math.sqrt(1 + pow(abs((self.end.x - self.start.x)/(self.end.y-self.start.y)),2))))
        except:
            dy = self.thickness * 1
        try:

            dx = int(self.thickness * 1/(math.sqrt(1 + pow(abs((self.end.x - self.start.x)/(self.end.y-self.start.y)),2))))
        except:
            dx = 0
        p1 = Point(self.start.x - dx, self.start.y - dy)
        p2 = Point(self.start.x + dx, self.start.y + dy)
        p3 = Point(self.end.x + dx, self.end.y + dy)
        p4 = Point(self.end.x -dx, self.end.y - dy)
        self.path = Polygon(p1,p2,p3,p4)
        self.path.setFill(color_rgb(156,94,89))
    def draw(self):
        self.path.draw(self.win)
    

    
