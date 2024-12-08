import sys
sys.setrecursionlimit(30000)

def solve():
    with open("6/6.txt", "r") as f:
        lines = f.readlines()
        lines = list(filter(lambda x : x.strip(), lines))
        lines = list(map(lambda x: x[:-1], lines))
        
        UP = (-1, 0)
        RIGHT = (0, 1)
        DOWN = (1, 0)
        LEFT = (0, -1)
        
        # Up = 0, Right = 1, Down = 2, Left = 3
        # Rotate = Direction Mod 4
        direction = 0
        checker = { 0: UP, 1: RIGHT, 2: DOWN, 3: LEFT }
        grid = lines
        seen = set()
        count = 0
        
        def move(y, x):
            nonlocal count
            nonlocal direction
            nonlocal seen  
            nonlocal checker
            nonlocal grid
            
            if (y, x) not in seen:
                seen.add((y, x))
                count += 1
                            
            checkY = checker[direction][0]
            checkX = checker[direction][1]
            
            if (checkY + y) < 0 or (checkY + y) >= len(grid) or (checkX + x) < 0 or (checkX + x) >= len(grid[0]):
                return  
            
            if grid[checkY + y][checkX + x] == "#":
                print(f"Changing Direction At {(y, x)}")
                direction = (direction + 1) % 4
                move(y, x)
                return
            

            move(checkY + y, checkX + x)
            return


        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "^":
                    move(y, x)
                    print(count)
                    return
                    
solve()