def countXMASGivenSource(grid, y, x):
    count = 0
    
    firstLeg = (grid[y - 1][x - 1] == "S" and grid[y + 1][x + 1] == "M") or (grid[y - 1][x - 1] == "M" and grid[y + 1][x + 1] == "S")
    
    secondLeg = (grid[y + 1][x - 1] == "S" and grid[y - 1][x + 1] == "M") or (grid[y + 1][x - 1] == "M" and grid[y - 1][x + 1] == "S")
    
    return firstLeg and secondLeg

with open("4/4.txt", "r") as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]
        
    count = 0
    
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == "A":
                count += countXMASGivenSource(grid, y, x)
                
    print(count)
                