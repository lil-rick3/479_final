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
        start_time = time.time()
        b1.move()
        if(b1.frame_ct % 1== 0):
            b1.repaint()
        time_taken = time.time() - start_time
        print(time_taken)
        time.sleep(max(0.01 - time_taken,0))
            
        
        
   
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

          
             
        
        
        
        
  

if __name__ =="__main__":
    main()
