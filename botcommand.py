from collections import deque
from pathfinder import *
class BotCommand():
    def __init__(self, edges, nodes, command_location):
        self.edge_dict = edges
        self.node_dict = nodes
        self.start = command_location
        self.requests = deque()
    def addRequests(self, newRequest):

        self.requests.append(newRequest)
    def giveRequest(self):
        if len(self.requests) == 0:
            return None
        else:
            
            sentRequest = self.requests.popleft()
            return getPath(self.edge_dict,self.node_dict, self.start, sentRequest.loc), sentRequest

    

