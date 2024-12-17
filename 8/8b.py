class NodeTracker():
    def __init__(self, board, height, width):
        self.board = board
        self.height = height
        self.width = width
        self.antinodes = set()
        self.node_sightings = {} # Key: Node ID, Value: (y,x)[]
        
    def add_antinode(self, y, x):
        if not (y >= 0 and y < self.height):
            return
        
        if not (x >= 0 and x < self.width):
            return
        
        self.antinodes.add((y, x))
        
    def count_antinodes(self):
        return len(self.antinodes)
    
    def in_bounds(self, y, x):
        return y >= 0 and y < self.height and x >= 0 and x < self.width
    
    def new_antinode(self, curr, ref):
        prev = self.antinodes
        
        curr_y, curr_x = curr
        ref_y, ref_x = ref
        
        y_diff = curr_y - ref_y
        x_diff = curr_x - ref_x
        times = 1
        
        new_y = curr_y + y_diff * times
        new_x = curr_x + x_diff * times
        
        while self.in_bounds(new_y, new_x):
            self.add_antinode(new_y, new_x)
            times += 1
            new_y = curr_y + y_diff * times
            new_x = curr_x + x_diff * times

    def solve(self):
        for y in range(self.height):
            for x in range(self.width):
                element = self.board[y][x]
                if element == ".":
                    continue
                
                if element not in self.node_sightings:
                    self.node_sightings[element] = [(y, x)]
                    continue 
                
                new_node = (y, x)
                for node in self.node_sightings[element]:
                    self.add_antinode(node[0], node[1])
                    self.new_antinode(new_node, node)
                    self.new_antinode(node, new_node)
                
                self.add_antinode(y, x)    
                self.node_sightings[element].append(new_node)

        return self 
    
    def display(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (y, x) in self.antinodes:
                    row = row + "#"
                else:
                    row = row + self.board[y][x]
            print(row)                

with open("8/8.txt", "r") as f:
    lines = list(map(lambda line : line.strip(), f.readlines()))
    height = len(lines)
    width = len(lines[0])
    node_tracker = NodeTracker(lines, height, width)
    node_tracker.solve()
    node_tracker.display()
    print(node_tracker.count_antinodes())