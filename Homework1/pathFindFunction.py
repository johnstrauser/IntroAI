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
            thisP_node.f = thisP_node.g + thisP_node.h

            # traverse the whole open_list to see whether to update f value
            for i in open_list:
                h = []
                h = i

                # if this position is in the open_list
                if h[1].position == this_position:

                    # if the f value which previous calculated is greater than the current one,
                    # update the f value
                    if h[0] > thisP_node.f:
                        h[0] = thisP_node.f

                        # sort the open_list because we changed the f value
                        heapq.heapify(open_list)

                        # set parent to be the current_node
                        h[1].parent = current_node

                # if not, add this node into the open_list
                else:
                    heapq.heappush(open_list, [thisP_node.f, thisP_node])

            # end of for loop, add current node into closed list
        closed_list.append(current_node)

        # print path on the agent board
        y = current_node.position[0]
        x = current_node.position[1]
        agentBoard[y][x] = "+"


        # pop from open_list(always the lowest f value because it's a priory queue)
        if len(open_list) != 0:
            sth = heapq.heappop(open_list)
            current_node = sth[1]
        else:
            return agentBoard







    





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
