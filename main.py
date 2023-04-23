from graphics import *
from node import Node
from edge import Edge
from board import Board
import time

WINDOW_WIDTH = 1700
WINDOW_HEIGHT = 1000
node_val = [(300,200),(400,300), (500,200), (300,400), (300, 400), (500, 400)]


def main():
    
    win = GraphWin("FOODIE", WINDOW_WIDTH, WINDOW_HEIGHT, autoflush=True)
    b1 = Board(win, WINDOW_WIDTH, WINDOW_HEIGHT)

    b1.repaint()

    while True:
        b1.move()
        time.sleep(30/1000)
        
        
   
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

          
             
        
        
        
        
  

if __name__ =="__main__":
    main()
