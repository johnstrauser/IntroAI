import random


class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(board, agent, target):
    agent_node = Node(None, agent)
    agent_node.g = 0
    agent_node.h = 0
    agent_node.f = 0
    target_node = Node(None, target)
    target_node.g = 0
    target_node.h = 0
    target_node.f = 0
    open_list = []
    closed_list = []

    open_list.append(agent_node)
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == target_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            reversedPath = list(reversed(path))
            return reversedPath

        next = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position[0] > (len(board) - 1) or node_position[0] < 0 or node_position[1] > (len(board[len(board) - 1]) - 1) or node_position[1] < 0:
                continue

            if board[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)
            next.append(new_node)

        for step in next:
            for closed_step in closed_list:
                if step == closed_step:
                    break
            step.g = current_node.g + 1
            step.h = (step.position[0] - target_node.position[0])**2 + \
                (step.position[1] - target_node.position[1])**2
            step.f = step.g + step.h

            for open_node in open_list:
                if step == open_node and step.g >= open_node.g:
                    break
            open_list.append(step)


def boardInit(n, m):
    "Initialize and return an empty 2d array for the board"
    "Array will be n x m"
    arr = [[0 for x in range(m)] for y in range(n)]
    for i in range(n):
        for j in range(m):
            # if j == 0 or j == m - 1:
            #   arr[i][j] = "X"
            # elif i == 0 or i == n - 1:
            #   arr[i][j] = "X"
            # else:
            #   arr[i][j] = 0
            arr[i][j] = 0
    return arr


def printBoard(arr, n, m):
    "print the board"
    print()
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print("")
    return


def updateAgentBoard(full, agent, loc, n, m):
    if full[loc[0] + 1][loc[1]] == "X":
        agent[loc[0] + 1][loc[1]] = "X"

    if full[loc[0] - 1][loc[1]] == "X":
        agent[loc[0] - 1][loc[1]] = "X"

    if full[loc[0]][loc[1] + 1] == "X":
        agent[loc[0]][loc[1] + 1] = "X"

    if full[loc[0]][loc[1] - 1] == "X":
        agent[loc[0]][loc[1] - 1] = "X"
    return


n, m = 50, 50
fullBoard = boardInit(n, m)
agentBoard = boardInit(n, m)

fileFound = 0
x = input("Enter an index for which maze to load: ")
fileRoot = ".\mazes\maze"
fileTail = ".txt"
fileName = fileRoot + str(x) + fileTail
file = open(fileName, "r")

allLines = file.readlines()
agentLoc = []
targetLoc = []
for i in range(len(allLines)):
    if i == 0:
        index = allLines[i].index(",")
        agentLoc.append(int(allLines[i][0:index]))
        agentLoc.append(int(allLines[i][index + 1:len(allLines[i])]))
        #fullBoard[agentLoc[0]][agentLoc[1]] = "a"
        #agentBoard[agentLoc[0]][agentLoc[1]] = "a"
    elif i == 1:
        index = allLines[i].index(",")
        targetLoc.append(int(allLines[i][0:index]))
        targetLoc.append(int(allLines[i][index + 1:len(allLines[i])]))
        #fullBoard[targetLoc[0]][targetLoc[1]] = "t"
        #agentBoard[targetLoc[0]][targetLoc[1]] = "t"
    else:
        index = allLines[i].index(",")
        tempX = int(allLines[i][0:index])
        tempY = int(allLines[i][index + 1:len(allLines[i])])
        fullBoard[tempX][tempY] = 1


print(str(agentLoc[0]) + "-" + str(agentLoc[1]))
print(str(targetLoc[0]) + "-" + str(targetLoc[1]))
updateAgentBoard(fullBoard, agentBoard, agentLoc, n, m)

printBoard(fullBoard, n, m)
agent = (agentLoc[0], agentLoc[1])
target = (targetLoc[0], targetLoc[1])
cont = 1
while (cont == 1):
    "Use A* to calculate new path for agent"
    path = astar(fullBoard, agent, target)
    print(path)
    "Move agent one space along path"

    "Update the 'vision' of the agent"

    "Check if agent has reached target"

    x = input("Enter 'n' for next step or 'q' for quit: ")
    if x == "q":
        cont = 0
