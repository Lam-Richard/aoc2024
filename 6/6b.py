import sys
sys.setrecursionlimit(500)

def solve():
    with open("6/6.txt", "r") as f:
        lines = f.readlines()
        lines = list(filter(lambda x : x.strip(), lines))
        lines = list(map(lambda x: [a for a in x[:-1]], lines))
        
        UP = (-1, 0)
        RIGHT = (0, 1)
        DOWN = (1, 0)
        LEFT = (0, -1)

        grid = lines
        
        def move(y, x):
            nonlocal direction
            nonlocal checker
            nonlocal grid
                            
            checkY = checker[direction][0]
            checkX = checker[direction][1]
            
            if (checkY + y) < 0 or (checkY + y) >= len(grid) or (checkX + x) < 0 or (checkX + x) >= len(grid[0]):
                return  
            
            if grid[checkY + y][checkX + x] == "#":
                direction = (direction + 1) % 4
                move(y, x)
                return
            

            while not((checkY + y) < 0 or (checkY + y) >= len(grid) or (checkX + x) < 0 or (checkX + x) >= len(grid[0])) and not (grid[checkY + y][checkX + x] == "#"):
                y = checkY + y
                x = checkX + x
                    
            move(y, x)
            return

        places = 0
        
        guardY = None
        guardX = None
        for y in range(len(grid)):
            if guardY:
                break
            for x in range(len(grid[0])):
                if grid[y][x] == "^":
                    guardY = y
                    guardX = x
                    break
                
                
        
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == ".":
                    grid[a][b] = "#"
                    try:
                        # Up = 0, Right = 1, Down = 2, Left = 3
                        # Rotate = Direction Mod 4
                        direction = 0
                        checker = { 0: UP, 1: RIGHT, 2: DOWN, 3: LEFT }
                        seen = set()
                        move(guardY, guardX)
                    except:
                        places += 1
                    grid[a][b] = "."
        print(places)             
                    
solve()