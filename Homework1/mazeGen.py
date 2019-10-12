import random
from pathlib import Path

def placeAgent(n,m):
    "pick a random x and y, place agent"
    output = []
    randX = int(random.random() * (n-3)) +1
    randY = int(random.random() * (m-3)) +1
    output.append(randX)
    output.append(randY)

    return output;
    
def placeTarget(agentLoc,n,m):
    "pick a random x and y, if agentLoc is not that random x and y, place agent"
    placed = 0
    output = []
    while (placed == 0):
        randX = int(random.random() * (n-3)) +1
        randY = int(random.random() * (m-3)) +1
        if agentLoc[0] != randX or agentLoc[1] != randY:
            output.append(randX)
            output.append(randY)
            placed = 1

    return output;

def writeBoard(agentLoc,targetLoc,n,m):
    x = input("Enter an index for the file name: ");
    data_folder = Path("./mazes/")
    fileNameRoot = "maze"
    fileTail = ".txt"
    fileName = fileNameRoot + str(x) + fileTail
    fullFilePath = data_folder / fileName
    
    file = open(fullFilePath,"w+");
    file.write(str(agentLoc[0])+","+str(agentLoc[1])+"\n");
    file.write(str(targetLoc[0])+","+str(targetLoc[1])+"\n");
    
    for i in range(1,n-1):
        for j in range(1,m-1):
            if (agentLoc[0] != i or agentLoc[1] != j) and (targetLoc[0] != i or targetLoc[1] != j):
                if random.random() > 0.7:
                    file.write(str(i)+","+str(j)+"\n");
            
    
    
    file.close();
    return;

n,m = 50,50;
agentLoc = placeAgent(n,m);
targetLoc = placeTarget(agentLoc,n,m);

writeBoard(agentLoc,targetLoc,n,m);