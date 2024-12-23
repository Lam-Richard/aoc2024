class Tracker():
    def __init__(self):
        self.trailheads = {} # Key: (y, x) of 0, Value: (y, x)[] of reachable 9
        self.lines = None
        self.height = None
        self.width = None
        self.res = None 
        
        with open("10/10.txt", "r") as f:
            lines = list(map(lambda line : line.strip(), f.readlines()))
            lines = list(map(lambda line : [int(i) for i in line], lines))
            
            self.lines = lines
            self.height = len(lines)
            self.width = len(lines[0])
            
    def adjacent(self, y, x):
        candidates = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
        
        candidates = list(filter(lambda pos : pos[0] >= 0 and pos[0] < self.height, candidates))
        
        candidates = list(filter(lambda pos : pos[1] >= 0 and pos[1] < self.width, candidates))
        
        return candidates
            
    def score_trailhead(self, start, curr):
        cy, cx = curr 
        val = self.lines[cy][cx]
        
        if self.lines[cy][cx] == 9:
            self.trailheads[start].add(curr)
            return 
        
        candidates = self.adjacent(cy, cx)
        for candidate in candidates:
            y, x = candidate
            if self.lines[y][x] == val + 1:
                self.score_trailhead(start, candidate)
                    
        return 
        
    def solve(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.lines[y][x] == 0 and (y, x) not in self.trailheads:
                    self.trailheads[(y, x)] = set()
                    self.score_trailhead((y, x), (y, x))
                    
        self.res = sum(map(lambda trailhead : len(self.trailheads[trailhead]), list(self.trailheads.keys())))
        return

    def print(self):
        print(self.res)

tracker = Tracker()
tracker.solve()
tracker.print()            
            
    
    