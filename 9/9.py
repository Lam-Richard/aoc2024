import sys
sys.setrecursionlimit(20000)

class Defragmenter():
    def contiguous_sum(self, start, offset):
        end_number = start + offset - 1
        return offset * (start + end_number) // 2
    
    def __init__(self):
        self.max_id = 0
        self.space = []  # (start idx, size of free space)[]
        self.files = [] # (start idx, size of file, file id)[]
        self.res = 0
        
        with open("9/9.txt", "r") as f:
            line = f.readlines()[0]
            
            self.files.append((0, int(line[0]), 0))
            self.max_id += 1
            
            for i in range(1, len(line)):
                char = line[i]
                
                # File
                if i % 2 == 0:
                    previous_end = self.space[-1][0] + self.space[-1][1]
                    self.files.append([previous_end, int(char), self.max_id])
                    self.max_id += 1
                
                # Space
                else:
                    previous_end = self.files[-1][0] + self.files[-1][1]
                    self.space.append([previous_end, int(char)])
                    
        self.curr_space = 0
        self.curr_files = 0
                 
    def fill_free_space(self):
        if self.files == []:
            return
        
        if self.space[self.curr_space][0] >= self.files[-1][0]:
            return 
        
        start_idx, free_space = self.space[self.curr_space]
        file_start, file_size, file_id = self.files[-1]
        
        if (file_size <= free_space):
            self.res += self.contiguous_sum(start_idx, file_size) * file_id
            new_free_space = free_space - file_size
            new_start_idx = start_idx + file_size
            self.space[self.curr_space] = [new_start_idx, new_free_space]
            self.files.pop(-1)
            self.fill_free_space()
            return
        
        self.res += self.contiguous_sum(start_idx, free_space) * file_id
        new_file_size = file_size - free_space
        self.files[-1] = [file_start, new_file_size, file_id]
        self.curr_space += 1
        self.fill_free_space()
        return
    
    def add_file(self):
        if self.curr_files >= len(self.files):
            return 
        
        file_start, file_size, file_id = self.files[self.curr_files]
        self.res += self.contiguous_sum(file_start, file_size) * file_id
        self.curr_files += 1
        self.add_file()
        return 
                    
    def solve(self):
        self.fill_free_space()
        self.add_file()
        
defragmenter = Defragmenter()
defragmenter.solve()
print(defragmenter.res)