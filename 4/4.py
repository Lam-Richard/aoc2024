def countXMASGivenSource(grid, y, x):
    count = 0
    
    minY = 0
    maxY = len(grid)
    
    minX = 0
    maxX = len(grid[0])
    
    # Left to Right
    if x + 3 < maxX:
        count += ([grid[y][i] for i in range(x, x + 4)] == [i for i in "XMAS"])   
        
    # Right to Left
    if x - 3 >= minX:
        rightToLeft = [grid[y][i] for i in range(x, x - 4, -1)]
        count += (rightToLeft == [i for i in "XMAS"])   
        
    # Top to Bottom
    if y + 3 < maxY:
        count += ([grid[i][x] for i in range(y, y + 4)] == [i for i in "XMAS"])
     
    # Bottom to Top   
    if y - 3 >= minY:
        count += ([grid[i][x] for i in range(y, y - 4, -1)] == [i for i in "XMAS"])
        
              
    # Left to Right & Top to Bottom
    if x + 3 < maxX and y + 3 < maxY:
        count += ([grid[y + i][x + i] for i in range(4)] == [i for i in "XMAS"])
 

    # Left to Right & Bottom to Top
    if x + 3 < maxX and y - 3 >= minY:
        count += ([grid[y - i][x + i] for i in range(4)] == [i for i in "XMAS"])
        
        
    # Right to Left & Top to Bottom
    if x - 3 >= minX and y + 3 < maxY:
        count += ([grid[y + i][x - i] for i in range(4)] == [i for i in "XMAS"])
 
 
    # Right to Left & Bottom to Top
    if x + 3 >= minX and y - 3 >= minY:
        count += ([grid[y - i][x - i] for i in range(4)] == [i for i in "XMAS"])    
        
    return count

with open("4/4.txt", "r") as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
        
    count = 0
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "X":
                count += countXMASGivenSource(grid, y, x)
                
    print(count)
                