def boardInit(n, m):
    "Initialize and return an empty 2d array for the board"
    "Array will be n x m"
    arr = [[0 for x in range(n)] for y in range(m)] 
    for i in range(n):
        for j in range(m):
            if j == 0 or j == m-1:
                arr[j][i] = "X"
            elif i == 0 or i == n-1:
                arr[j][i] = "X"
            else:
                arr[j][i] = " "
            print(arr[j][i], end=" ")
        print("")
    return arr;

def printBoard(arr,n,m):
    "print the board"
    print()
    for i in range(n):
        for j in range(m):
            print(arr[j][i], end=" ")
        print("")
    return;

n,m = 10,10;
arr = boardInit(n,m);
printBoard(arr,n,m);