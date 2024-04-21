import sys
sys.setrecursionlimit(150000000)

grid=[[0,4,0,8,0,0,0,0,5],
      [5,0,0,0,0,2,0,0,0],
      [0,2,7,0,4,0,0,0,1],
      [0,0,0,0,5,0,8,2,0],
      [2,0,8,3,9,6,0,0,4],
      [7,0,0,0,8,4,1,6,0],
      [1,0,5,0,6,0,4,9,0],
      [9,0,2,0,0,0,3,0,7],
      [3,7,0,9,0,8,5,1,0]]

def solve(grid):
    

    position=get_empty(grid)
    if not position:
        return True
    else:
        row,column=position

    for i in range(1,10):
        if validatate(grid,i,(row,column)):
            
            grid[row][column]=i
            
            if solve(grid):
                return True

            grid[row][column]=0
    return False

def validatate(grid,num,pos):
    
    #Checking Row
    for i in range(9):
        if grid[pos[0]][i]==num and pos[1]!=i:
            return False
    
    #Checking Column
    for i in range(9):
        if grid[i][pos[1]]==num and pos[0]!=i:
            return False
        
    #Checking the 3x3
    box_x=pos[1]//3
    box_y=pos[0]//3

    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if grid[i][j]==num and (i,j)!=pos:
                return False
            
    return True

def print_grid(grid):
    for i in range(9):
        print(grid[i])
    print('')


def get_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return(i,j)
    return None       
        




print_grid(grid)
print('')
solve(grid)

print_grid(grid)