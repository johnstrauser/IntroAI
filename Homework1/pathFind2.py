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


#   def __eq__(self, other):
#       return self.position == other.position

def getInsertLoc(list, f):
    # print("In the IL length of OL is", len(list))
    if len(list) == 0:
        return 0
    for i in range(len(list)):
        a = []
        # print("In the IL length of a is", a)
        a = list[i]
        #  print("In the IL length of a is", a)
        # print("In the IL length of a[0] is", a[0])
        # print("In the IL f is", f)
        if (a[0] > f):
            return i
    return i + 1
    # use with list.insert(getInsertLoc(list,new_node.f),new_node)


def boardInit(n, m, walls):
    # Initialize and return an empty 2d array for the board
    # Array will be n x m
    arr = [[0 for x in range(m)] for y in range(n)]
    for i in range(n):
        for j in range(m):
            if j == 0 or j == m - 1:
                arr[i][j] = "X"
            elif i == 0 or i == n - 1:
                arr[i][j] = "X"
            elif random.random() > 0.7 and walls == 1:
                arr[i][j] = "X"
            else:
                arr[i][j] = " "
            # print(arr[j][i], end=" ")
        # print("")"
    return arr;


def printBoard(arr, n, m):
    # print the board
    print()
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print("")
    return;


def placeAgent(arr, n, m):
    "pick a random x and y, if no wall there, place agent"
    placed = 0
    output = []
    while (placed == 0):
        randX = int(random.random() * (n - 3)) + 1
        randY = int(random.random() * (m - 3)) + 1
        if arr[randX][randY] == " ":
            arr[randX][randY] = "a"
            output.append(randX)
            output.append(randY)
            placed = 1

    return output;


def placeTarget(arr, n, m):
    "pick a random x and y, if no wall there, place agent"
    placed = 0
    output = []
    while (placed == 0):
        randX = int(random.random() * (n - 3)) + 1
        randY = int(random.random() * (m - 3)) + 1
        if arr[randX][randY] == " ":
            arr[randX][randY] = "t"
            output.append(randX)
            output.append(randY)
            placed = 1

    return output;


def updateAgentBoard(arr, arr2, loc, n, m):
    if arr[loc[0] + 1][loc[1]] == "X":
        arr2[loc[0] + 1][loc[1]] = "X"

    if arr[loc[0] - 1][loc[1]] == "X":
        arr2[loc[0] - 1][loc[1]] = "X"

    if arr[loc[0]][loc[1] + 1] == "X":
        arr2[loc[0]][loc[1] + 1] = "X"

    if arr[loc[0]][loc[1] - 1] == "X":
        arr2[loc[0]][loc[1] - 1] = "X"
    return;


def updatePath(agentBoard, agentLoc, targetLoc):
    y_axis_diff = agentLoc[0] - targetLoc[0]
    x_axis_diff = agentLoc[1] - targetLoc[1]


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
        # print("currentnode position ", current_node.position)

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            this_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            print(this_position)

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
                # print(thisP_node.f)
                a = getInsertLoc(open_list, thisP_node.f)
                print("i am a ", a)
                open_list.insert(a, [thisP_node.f, thisP_node])
                print(open_list)

                """" this is for update f value, might have more bug in it ...
                k = 0
                # traverse the whole open_list to see whether to update f value
                for i in open_list:
                    h = []
                    h = i

                    # if this position is in the open_list
                    if h[1].position == this_position:
                        k = 1

                    if (k == 1):
                        if h[0] > thisP_node.f:
                            open_list.remove([thisP_node.f, thisP_node])
                            h[0] = thisP_node.f
                            open_list.insert(getInsertLoc(open_list, thisP_node.f), [thisP_node.f, thisP_node])
                            h[1].parant = current_node
                    else:
                        # add this node to open_list
                        # print(open_list)
                        # print(thisP_node.f)
                        # heapq.heappush(open_list, (thisP_node.f, thisP_node))
                        open_list.insert(getInsertLoc(open_list, thisP_node.f), [thisP_node.f, thisP_node])"""""
        # end of for loop, add current node into closed list
        closed_list.append(current_node)
        # print path on the agent board
        y = current_node.position[0]
        x = current_node.position[1]
        agentBoard[y][x] = "+"
        # pop from open_list(always the lowest f value because it's a priory queue)
        print(len(open_list))
        if current_node.position != target_node.position:
            sth = []
            sth = open_list.pop(0)
            current_node = sth[1]
        else:
            return agentBoard

    return agentBoard


# tests, returns
n, m = 10, 10;
fullBoard = boardInit(n, m, 1);
agentBoard = boardInit(n, m, 0);
"place agent and target"
agentLoc = placeAgent(fullBoard, n, m);
print(agentLoc)
agentBoard[agentLoc[0]][agentLoc[1]] = "a";
targetLoc = placeTarget(fullBoard, n, m);
print(targetLoc)
agentBoard[targetLoc[0]][targetLoc[1]] = "t";
updateAgentBoard(fullBoard, agentBoard, agentLoc, n, m);
printBoard(fullBoard, n, m);
printBoard(agentBoard, n, m);

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

printBoard(agentBoard, n, m)
