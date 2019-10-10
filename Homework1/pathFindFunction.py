import random
import heapq
import math

class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def findPath(open_list, closed_list, agent_node, target_node, fullBoard, agentBoard):

    if agent_node.position == target_node.position:
        return 0

    # make the start vertex current
    current_node = Node(None, agent_node.position)

    # calculate the h value for the start(current) node
    current_node.h = abs(current_node.position[0] - target_node.position[0]) \
                     + abs(current_node.position[1] - target_node.position[1])

    # calculate the f value for the start(current) node
    current_node.f = current_node.g + current_node.h

    while current_node.position != target_node.position:

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            this_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

        # if this position [a, b] in the agentboard is not blocked
        # and is not in closed list
        # and is not in open list
        if agentBoard[this_position[0]][this_position[1]] != "X" \
                and this_position not in closed_list \
                and this_position not in open_list:

            # create node for this position
            thisP_node = Node(current_node, this_position)
            thisP_node.g = current_node.g + 1
            thisP_node.h = abs(thisP_node.position[0] - target_node.position[0]) \
                     + abs(thisP_node.position[1] - target_node.position[1])
            thisP_node.f = g + h

            # add this position into the open list, ordered by their f value
            heapq.heappush(open_list, (thisP_node.f, thisP_node))






    





# initialization of open/closed lists and object agent and target
open_list = []
closed_list = []
agent_node = Node(None, agentLoc)
agent_node.g = 0
agent_node.h = 0
agent_node.f = 0
target_node = Node(None, targetLoc)
target_node.g = 0
target_node.h = 0
target_node.f = 0
findPath(open_list, closed_list, agent_node, target_node, fullBoard, agentBoard)
