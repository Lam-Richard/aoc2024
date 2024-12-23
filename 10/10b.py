# This next problem is DP - if the ratings of a trailhead is the number of distinct paths starting from one trailhead, and we want the sum of the ratings, then we want the number of distinct paths starting from ALL trailheads.

# What we want to answer is, starting at some index, what are all the ways to reach a 9?

# The base is, if self.grid[y][x] == 9, then the answer is 1. 

# Indices with a value of 8 will have answers of sum(value of 9s around me)
# Indices with a value of 7 will have answers of sum(value of 8s around me)
# . . . and so on.

# Because we want to make sure the paths start all the way to 0, we will only add the value of 0s to the total sum.

class Tracker():
    def __init__(self):
        self.res = 0 
        self.lines = None
        self.height = None
        self.width = None
        self.dp = None
        self.by_value = {} # Key: Integer Value, Value: (y, x)[]
        
        with open("10/10.txt", "r") as f:
            lines = list(map(lambda line : line.strip(), f.readlines()))
            lines = list(map(lambda line : [int(i) for i in line], lines))
            
            self.lines = lines
            self.height = len(lines)
            self.width = len(lines[0])

            self.dp = [[[0] for i in range(self.width)] for j in range(self.height)]
            
    def adjacent(self, y, x):
        candidates = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
        
        candidates = list(filter(lambda pos : pos[0] >= 0 and pos[0] < self.height, candidates))
        
        candidates = list(filter(lambda pos : pos[1] >= 0 and pos[1] < self.width, candidates))
        
        return candidates
                
            
    def solve(self):
        for y in range(self.height):
            for x in range(self.width):
                
                if self.lines[y][x] == 9:
                    self.dp[y][x] = 1
                    continue
            
                val = self.lines[y][x]
                
                self.by_value[val] = self.by_value.get(val, []) + [(y, x)]
                
        for num in range(8, -1, -1):
            vals = self.by_value[num]
            
            for vy, vx in vals:
                temp = 0
                candidates = self.adjacent(vy, vx)
                
                for cy, cx in candidates:
                    if self.lines[cy][cx] == num + 1:
                        temp += self.dp[cy][cx]
                        
                self.dp[vy][vx] = temp
                
        zero_vals = self.by_value[0]
        for zy, zx in zero_vals:
            self.res += self.dp[zy][zx]
            
    def print(self):
        print(self.res)
        
        
tracker = Tracker()
tracker.solve()
tracker.print()