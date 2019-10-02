import random

def boardInit(n, m, walls):
    "Initialize and return an empty 2d array for the board"
    "Array will be n x m"
    arr = [[0 for x in range(m)] for y in range(n)] 
    for i in range(n):
        for j in range(m):
            if j == 0 or j == m-1:
                arr[i][j] = "X"
            elif i == 0 or i == n-1:
                arr[i][j] = "X"
            elif random.random() > 0.7 and walls == 1:
                arr[i][j] = "X"
            else:
                arr[i][j] = " "
            "print(arr[j][i], end=" ")"
        "print("")"
    return arr;

def printBoard(arr,n,m):
    "print the board"
    print()
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print("")
    return;
    
def placeAgent(arr,n,m):
    "pick a random x and y, if no wall there, place agent"
    placed = 0
    output = []
    while (placed == 0):
        randX = int(random.random() * (n-3)) +1
        randY = int(random.random() * (m-3)) +1
        if arr[randX][randY] == " ":
            arr[randX][randY] = "a"
            output.append(randX)
            output.append(randY)
            placed = 1

    return output;
    
def placeTarget(arr,n,m):
    "pick a random x and y, if no wall there, place agent"
    placed = 0
    output = []
    while (placed == 0):
        randX = int(random.random() * (n-3)) +1
        randY = int(random.random() * (m-3)) +1
        if arr[randX][randY] == " ":
            arr[randX][randY] = "t"
            output.append(randX)
            output.append(randY)
            placed = 1

    return output;

def updateAgentBoard(arr,arr2,loc,n,m):
    if arr[loc[0]+1][loc[1]] == "X":
        arr2[loc[0]+1][loc[1]] = "X"
        
    if arr[loc[0]-1][loc[1]] == "X":
        arr2[loc[0]-1][loc[1]] = "X"
        
    if arr[loc[0]][loc[1]+1] == "X":
        arr2[loc[0]][loc[1]+1] = "X"
        
    if arr[loc[0]][loc[1]-1] == "X":
        arr2[loc[0]][loc[1]-1] = "X"
    return;
    
    
n,m = 10,10;
fullBoard = boardInit(n,m,1);
agentBoard = boardInit(n,m,0);

"place agent and target"
agentLoc = placeAgent(fullBoard,n,m);
agentBoard[agentLoc[0]][agentLoc[1]] = "a";
targetLoc = placeTarget(fullBoard,n,m);
agentBoard[targetLoc[0]][targetLoc[1]] = "t";
updateAgentBoard(fullBoard,agentBoard,agentLoc,n,m);

printBoard(fullBoard,n,m);
printBoard(agentBoard,n,m);

cont = 1;
while (cont == 1):
    "Use A* to calculate new path for agent"
    
    "Move agent one space along path"
    
    "Update the 'vision' of the agent"
    
    "Check if agent has reached target"

    x = input("Enter 'n' for next step or 'q' for quit.");
    if x == "q":
        cont= 0;
    

