import random

def boardInit(n, m):
    "Initialize and return an empty 2d array for the board"
    "Array will be n x m"
    arr = [[0 for x in range(m)] for y in range(n)] 
    for i in range(n):
        for j in range(m):
            if j == 0 or j == m-1:
                arr[i][j] = "X"
            elif i == 0 or i == n-1:
                arr[i][j] = "X"
            else:
                arr[i][j] = " "
    return arr;

def printBoard(arr,n,m):
    "print the board"
    print()
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print("")
    return;


def updateAgentBoard(full,agent,loc,n,m):
    if full[loc[0]+1][loc[1]] == "X":
        agent[loc[0]+1][loc[1]] = "X"
        
    if full[loc[0]-1][loc[1]] == "X":
        agent[loc[0]-1][loc[1]] = "X"
        
    if full[loc[0]][loc[1]+1] == "X":
        agent[loc[0]][loc[1]+1] = "X"
        
    if full[loc[0]][loc[1]-1] == "X":
        agent[loc[0]][loc[1]-1] = "X"
    return;
    
    
n,m = 50,50;
fullBoard = boardInit(n,m);
agentBoard = boardInit(n,m);

fileFound = 0
x = input("Enter an index for which maze to load: ");
fileRoot = ".\mazes\maze";
fileTail = ".txt";
fileName = fileRoot + str(x) + fileTail;
file = open(fileName,"r");
   
allLines = file.readlines();
agentLoc = [];
targetLoc = [];
for i in range(len(allLines)):
    if i == 0:
        index = allLines[i].index(",");
        agentLoc.append(int(allLines[i][0:index]));
        agentLoc.append(int(allLines[i][index+1:len(allLines[i])]));
        fullBoard[agentLoc[0]][agentLoc[1]] = "a";
        agentBoard[agentLoc[0]][agentLoc[1]] = "a";
    elif i == 1:
        index = allLines[i].index(",");
        targetLoc.append(int(allLines[i][0:index]));
        targetLoc.append(int(allLines[i][index+1:len(allLines[i])]));
        fullBoard[targetLoc[0]][targetLoc[1]] = "t";
        agentBoard[targetLoc[0]][targetLoc[1]] = "t";
    else:
        index = allLines[i].index(",");
        tempX = int(allLines[i][0:index]);
        tempY = int(allLines[i][index+1:len(allLines[i])]);
        fullBoard[tempX][tempY] = "X";
        

print(str(agentLoc[0])+"-"+str(agentLoc[1]));
print(str(targetLoc[0])+"-"+str(targetLoc[1]));
updateAgentBoard(fullBoard,agentBoard,agentLoc,n,m);
printBoard(fullBoard,n,m);
printBoard(agentBoard,n,m);

cont = 1;
while (cont == 1):
    "Use A* to calculate new path for agent"
    
    "Move agent one space along path"
    
    "Update the 'vision' of the agent"
    
    "Check if agent has reached target"

    x = input("Enter 'n' for next step or 'q' for quit: ");
    if x == "q":
        cont= 0;
    

