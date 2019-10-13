import random
import math
import heapq
from pathlib import Path

class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        if self.f != other.f:
            return self.f < other.f
        else:
            #if two f values are equal, use g value
            #flip this '<' to '>' for tiebreaker part of assignment
            return self.g < other.g
                


def aStar(start_loc, end_loc, board):
    open_list = []
    closed_list = []
    start_node = Node(None, start_loc)
    end_node = Node(None, end_loc)
    count = 0
    
    current_node = start_node
    # calculate the h value for the start(current) node
    current_node.h = abs(end_node.position[0] - current_node.position[0]) + abs(end_node.position[1] - current_node.position[1])

    # calculate the f value for the start(current) node
    current_node.f = current_node.g + current_node.h
    #while the current node is not the target node, loop
    while (current_node.position[0] != end_loc[0] or current_node.position[1] != end_loc[1]):
        #generate all possiblie expansions of current node in for loop
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            #calc new location
            new_loc = [current_node.position[0]+new_position[0],current_node.position[1]+new_position[1]]
            #if the new node is not a wall and has not already been closed, either update its f value and parent or add to open list
            if board[new_loc[0]][new_loc[1]] != "X" and indexOf(closed_list, new_loc) == -1:
                #initialize new node
                new_node = Node(current_node, new_loc)
                new_node.g = current_node.g + 1
                new_node.h = abs(end_node.position[0] - new_node.position[0]) + abs(end_node.position[1] - new_node.position[1])
                new_node.f = new_node.g + new_node.h
                #get index of new node in open list
                index = indexOf(open_list,new_node.position)
                if index != -1:
                    #if node exists in open list, check if the f value is better
                    if open_list[index].f > new_node.f:
                        #if f value is better, replace and sort
                        open_list[index] = new_node
                        heapq.heapify(open_list)
                        
                else:
                    #if node is not in open list, add to open list
                    #line below this is for tiebreaker in favor of larger g val
                    #heapq.heappush(open_list,(new_node.f,new_node.g*(-1),new_node))
                    #line below this is for tiebreaker in favor of smaller g val
                    heapq.heappush(open_list,new_node)
                    
        #current node has been completely expanded, add to closed list
        closed_list.append(current_node)
        count += 1
        #smallest f value should be the first index of the list
        if len(open_list) == 0:
            return -1
        else:
            current_node = heapq.heappop(open_list)
            
    
    #at this point either there is no possible path and the function has returned -1
    #or the while loop has ended and current node should now be end node
    #we can now draw the "+" by tracing back through the list of parents
    
    current_node = current_node.parent
    while (current_node.position[0] != start_loc[0] or current_node.position[1] != start_loc[1]):
        agentBoard[current_node.position[0]][current_node.position[1]] = "+"
        current_node = current_node.parent
    #return count to indicate completion
    return count
    
def adapAStar(start_loc, end_loc, board, old_closed_list):
    open_list = []
    closed_list = []
    start_node = Node(None, start_loc)
    end_node = Node(None, end_loc)
    count = 0
    
    current_node = start_node
    # calculate the h value for the start(current) node
    old_index = indexOf(old_closed_list, start_loc)
    old_target_index = indexOf(old_closed_list, end_loc)
    if old_index == -1:
        current_node.h = abs(end_node.position[0] - current_node.position[0]) + abs(end_node.position[1] - current_node.position[1])
    else:
        current_node.h = (old_closed_list[old_target_index].g) - (old_closed_list[old_index].g)

    # calculate the f value for the start(current) node
    current_node.f = current_node.g + current_node.h
    #while the current node is not the target node, loop
    while (current_node.position[0] != end_loc[0] or current_node.position[1] != end_loc[1]):
        #generate all possiblie expansions of current node in for loop
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            #calc new location
            new_loc = [current_node.position[0]+new_position[0],current_node.position[1]+new_position[1]]
            #if the new node is not a wall and has not already been closed, either update its f value and parent or add to open list
            if board[new_loc[0]][new_loc[1]] != "X" and indexOf(closed_list, new_loc) == -1:
                #initialize new node
                new_node = Node(current_node, new_loc)
                new_node.g = current_node.g + 1
                old_index = indexOf(old_closed_list, new_loc)
                if old_index == -1:
                    new_node.h = abs(end_node.position[0] - new_node.position[0]) + abs(end_node.position[1] - new_node.position[1])
                else:
                    new_node.h = (old_closed_list[old_target_index].g) - (old_closed_list[old_index].g)
                new_node.f = new_node.g + new_node.h
                #get index of new node in open list
                index = indexOf(open_list,new_node.position)
                if index != -1:
                    #if node exists in open list, check if the f value is better
                    if open_list[index].f > new_node.f:
                        #if f value is better, replace and sort
                        open_list[index] = new_node
                        heapq.heapify(open_list)
                        
                else:
                    #if node is not in open list, add to open list
                    #line below this is for tiebreaker in favor of larger g val
                    #heapq.heappush(open_list,(new_node.f,new_node.g*(-1),new_node))
                    #line below this is for tiebreaker in favor of smaller g val
                    heapq.heappush(open_list,new_node)
                    
        #current node has been completely expanded, add to closed list
        closed_list.append(current_node)
        count += 1
        #smallest f value should be the first index of the list
        if len(open_list) == 0:
            return -1,[]
        else:
            current_node = heapq.heappop(open_list)
            
    
    #at this point either there is no possible path and the function has returned -1
    #or the while loop has ended and current node should now be end node
    #we can now draw the "+" by tracing back through the list of parents
    
    current_node = current_node.parent
    while (current_node.position[0] != start_loc[0] or current_node.position[1] != start_loc[1]):
        agentBoard[current_node.position[0]][current_node.position[1]] = "+"
        current_node = current_node.parent
    #return count to indicate completion
    old_closed_list = closed_list
    return count, old_closed_list
        
def indexOf(list, loc):
    #check if loc exists in list, i if true, -1 if false
    if len(list) == 0:
        return -1
    for i in range(len(list)):
        if list[i].position[0] == loc[0] and list[i].position[1] == loc[1]:
            return i
    return -1

def boardInit(n, m):
    "Initialize and return an empty 2d array for the board"
    "Array will be n x m"
    arr = [[0 for x in range(m)] for y in range(n)]
    for i in range(n):
        for j in range(m):
            if j == 0 or j == m - 1:
              arr[i][j] = "X"
            elif i == 0 or i == n - 1:
              arr[i][j] = "X"
            else:
              arr[i][j] = " "
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

def availablePath(agentBoard,agentLoc):
    if agentBoard[agentLoc[0] + 1][agentLoc[1]] == "+" or agentBoard[agentLoc[0] + 1][agentLoc[1]] == "t":
        agentBoard[agentLoc[0]][agentLoc[1]] = " "
        agentLoc[0] += 1
        agentBoard[agentLoc[0]][agentLoc[1]] = "a"
        return 1
    elif agentBoard[agentLoc[0] - 1][agentLoc[1]] == "+" or agentBoard[agentLoc[0] - 1][agentLoc[1]] == "t":
        agentBoard[agentLoc[0]][agentLoc[1]] = " "
        agentLoc[0] -= 1
        agentBoard[agentLoc[0]][agentLoc[1]] = "a"
        return 1
    elif agentBoard[agentLoc[0]][agentLoc[1] + 1] == "+" or agentBoard[agentLoc[0]][agentLoc[1] + 1] == "t":
        agentBoard[agentLoc[0]][agentLoc[1]] = " "
        agentLoc[1] += 1
        agentBoard[agentLoc[0]][agentLoc[1]] = "a"
        return 1
    elif agentBoard[agentLoc[0]][agentLoc[1] - 1] == "+" or agentBoard[agentLoc[0]][agentLoc[1] - 1] == "t":
        agentBoard[agentLoc[0]][agentLoc[1]] = " "
        agentLoc[1] -= 1
        agentBoard[agentLoc[0]][agentLoc[1]] = "a"
        return 1
    return 0

def removePath(board,n,m):
    for i in range(n):
        for j in range(m):
            if board[i][j] == "+":
                board[i][j] = " "
        
    return

n, m = 101, 101
fullBoard = boardInit(n, m)
agentBoard = boardInit(n, m)

fileFound = 0
x = input("Enter an index for which maze to load: ")
data_folder = Path("./mazes/")
fileNameRoot = "maze"
fileTail = ".txt"
fileName = fileNameRoot + str(x) + fileTail
fullFilePath = data_folder / fileName
file = open(fullFilePath, "r")

allLines = file.readlines()
agentLoc = []
targetLoc = []
for i in range(len(allLines)):
    if i == 0:
        index = allLines[i].index(",")
        agentLoc.append(int(allLines[i][0:index]))
        agentLoc.append(int(allLines[i][index + 1:len(allLines[i])]))
        fullBoard[agentLoc[0]][agentLoc[1]] = "a"
        agentBoard[agentLoc[0]][agentLoc[1]] = "a"
    elif i == 1:
        index = allLines[i].index(",")
        targetLoc.append(int(allLines[i][0:index]))
        targetLoc.append(int(allLines[i][index + 1:len(allLines[i])]))
        fullBoard[targetLoc[0]][targetLoc[1]] = "t"
        agentBoard[targetLoc[0]][targetLoc[1]] = "t"
    else:
        index = allLines[i].index(",")
        tempX = int(allLines[i][0:index])
        tempY = int(allLines[i][index + 1:len(allLines[i])])
        fullBoard[tempX][tempY] = "X"


print(str(agentLoc[0]) + "-" + str(agentLoc[1]))
print(str(targetLoc[0]) + "-" + str(targetLoc[1]))
updateAgentBoard(fullBoard, agentBoard, agentLoc, n, m)

printBoard(fullBoard, n, m)
#printBoard(agentBoard,n,m)

count = 0
cont = 1
old_closed_list = []
while (cont > 0):
    "Use A* to calculate new path for agent"
    if availablePath(agentBoard,agentLoc) > 0:
        #move agent to + on agent board
        #update agentLoc
        #above is done in availablePath()
        
        #add + to fulllBoard in agentloc
        if agentLoc[0] != targetLoc[0] or agentLoc[1] != targetLoc[1]:
            fullBoard[agentLoc[0]][agentLoc[1]] = "+"
        #update agent vision on agent board
        updateAgentBoard(fullBoard, agentBoard, agentLoc, n, m)
        #printBoard(fullBoard,n,m)
        if cont != 2:
            printBoard(agentBoard,n,m)
    else:
        #ensure there are no + on board
        removePath(agentBoard,n,m)
        #run a* to generate new path
        
        #below is forward a*
        #out = aStar(agentLoc, targetLoc, agentBoard)
        #below is backward a*
        #out = aStar(targetLoc, agentLoc, agentBoard)
        #below is adaptive a*
        out, old_closed_list = adapAStar(agentLoc, targetLoc, agentBoard, old_closed_list)
        
        if cont != 2:
            printBoard(agentBoard,n,m)
        if out == -1:
            print("No path could be found from the agent to the target.")
            cont = -1
            break;
        else:
            count += out
        

    if agentLoc[0] == targetLoc[0] and agentLoc[1] == targetLoc[1]:
        printBoard(fullBoard,n,m)
        print("Count of expanded nodes: "+str(count))
        cont = 0
    if cont == 1:
        x = input("Enter 'n' for next step, 'f' to skip to the final output, or 'q' for quit: ")
        if x == "q":
            cont = 0
        elif x == "f":
            cont = 2
