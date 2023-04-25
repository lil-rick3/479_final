from graphics import *
from node import Node
from edge import Edge
from grid import Grid
from bot import Bot
from pathfinder import *
from botcommand import BotCommand
from request import Request
import random
class Board():
    def __init__(self, window, width, height):
        self.window_width = width
        self.window_height = height
        #nodeval is a series of nodes, based on position don't chanfe node_val array
        self.node_val = [(300+100,400),(400+100,500),(500+100,400), (300+100,600), (500+100, 600), (100+100,300), (100+100,100), (300+100,100), (300+100,300), (900+100,400),\
                         (900+100,600),(1500+100, 400), (1500+100, 600), (500+100, 100), (700+100,400), (700+100,100), (900+100,100),(1200+100, 400), (1200+100,100), (1500+100,100),\
                            (1500+100, 900), (1200+100, 600),(900+100,900), (1200+100, 900), (700+100,900), (500+100, 900), (700+100, 600), (100+100,700), (100,600), (100,400),\
                                (100,900), (300,900),(800,200),(700,200)]
        self.edges = [(0,1), (0,2), (1,2), (0,3), (3,1), (3,4), (2,4),(1,4), (0,5), (5,29),\
                    (5,6), (6,7), (7,8), (0,8), (29,28), (28,27), (27,3), (27,30), (27,31), (30,31),\
                    (31,25), (25,24), (4,25), (24,22), (22,23), (23, 20), (21,20), (4,26), (26,10), (10,21),\
                     (9,10), (2,14),(14,9),(9,17),(17,11),(21,12),(11,12), (10,22),(12,20), (7,13),\
                        (13,15),(15,16),(16,18),(16,9),(18,17),(18,19),(19,11),(15,32),(32,14),(32,33)]
        self.win = window
        self.node_dict = {}
        self.edgeList = {}
        self.grid = Grid(self.window_width, self.window_height, 100, self.win)
        self.old_main = Image(Point(150+100,500), "img/old_main.png")
        self.mall = Rectangle(Point(300+100,400), Point(self.window_width, 600))
        self.mall.setFill(color_rgb(25,125,52))
        self.union = Image(Point(600,290), "img/student_union.png")
        self.admissions = Image(Point(900,260), "img/admissions.png")
        self.background = Rectangle(Point(0,0), Point(self.window_width, self.window_height))
        self.background.setFill(color_rgb(0,0,0))
        self.frame_ct = 0
        self.request = []
        
        
        self.createNodes()
        self.createEdges()
        self.init_paint()

        self.botBrain = BotCommand(self.edgeList, self.node_dict, 33)
        
        
        thing = getPath(self.edgeList, self.node_dict, 33, 3, len(self.node_dict))
        self.testBot = Bot(self.node_dict[33], self.win, self.edgeList)
        self.testBot.setPath(thing)
        
    def move(self):
        self.testBot.move()
        self.frame_ct += 1
        self.make_requets()
        self.repaint()
    def init_paint(self):
        self.background.draw(self.win)
        self.old_main.draw(self.win)
        self.mall.draw(self.win)
        self.union.draw(self.win)
        self.admissions.draw(self.win)
        self.paintEdges()
        self.paintNodes()
        self.grid.draw()

    def repaint(self):
        
       
        self.testBot.draw()


    def paintNodes(self):
    
        for key in self.node_dict:
            self.node_dict[key].draw()
    def paintEdges(self):
        for key in self.edgeList:
            self.edgeList[key].draw()
    def createNodes(self):
        i = 0
        for coord_tuple in self.node_val:
            tempNode = Node(coord_tuple[0], coord_tuple[1], self.win, i)
            self.node_dict[i] = tempNode
            i += 1

    def createEdges(self):
        for edgeTuple in self.edges:
            id = str(edgeTuple[0]) + "," + str(edgeTuple[1])
            tempEdge = Edge(self.node_dict[edgeTuple[0]], self.node_dict[edgeTuple[1]], self.win,id)
            self.edgeList[id] = tempEdge
            id = str(edgeTuple[1]) + "," + str(edgeTuple[0])
            tempEdge = Edge(self.node_dict[edgeTuple[1]], self.node_dict[edgeTuple[0]], self.win,id)
            self.edgeList[id] = tempEdge
    def make_requets(self):
        if (self.frame_ct % 10) == 0:
            self.request.append(Request(random.randint(0,len(self.node_dict) - 2),self.node_dict, self.win))

            

    

