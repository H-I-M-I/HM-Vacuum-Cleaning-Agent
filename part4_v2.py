import random

class GridSimulation:
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[False for _ in range(cols)] for _ in range(rows)]
        self.total_performance = 0

        self.hurdles = []
        self.extra_moves = {}  

    '''def place_dirt(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col] = random.choice([False, True])'''
    
    def place_dirt(self):
        dirt_positions = [(2, 2)]
        for x, y in dirt_positions:
            self.grid[y][x] = True

    def place_hurdles(self, hurdle_rate=0.125):
        num_hurdles = int(self.rows * self.cols * hurdle_rate)
        possible_locations = [(x, y) for y in range(self.rows) for x in range(self.cols)]

        # self.hurdles = random.sample(possible_locations, num_hurdles)
        self.hurdles.append((1, 2)) 
        self.hurdles.append((2, 1))
        
        for (x, y) in self.hurdles:
            self.grid[y][x] = 999

    def clean_tile(self):
        self.grid[self.agent_y][self.agent_x] = False

    def move_agent(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            if self.grid[y][x]:
                print(" ")
            elif (x, y) in self.hurdles:
                print(" ")
            else:
                self.agent_x = x
                self.agent_y = y
        else:
            print("Agent cannot move out of bounds.")

    def clean_partition(self):
        print("Before Cleaning:")
        self.print_grid()

        self.agent_x = random.randint(0, self.cols - 1)
        self.agent_y = random.randint(0, self.rows - 1)
        while (self.agent_x, self.agent_y) in self.hurdles:
            self.agent_x = random.randint(0, self.cols - 1)
            self.agent_y = random.randint(0, self.rows - 1)
            
        print(f"Agent Initial Position: ({self.agent_x}, {self.agent_y})\n")
        
        partition_performance = 16
        
        for y in range(self.rows):
            for x in range(self.cols):
                if (x, y) in self.hurdles:
                    alternative_moves = self.find_alternative_moves(x, y)
                    if alternative_moves:
                        self.extra_moves[(y, x)] = alternative_moves
                        print(f"Hurdle at ({y}, {x}), Alternative Paths:")
                        for path in alternative_moves:
                            print(path)
                        min_moves = min(alternative_moves, key=len)
                        if min_moves:
                            print(f"Chosen Path: {min_moves}")
                            self.move_agent(*min_moves[0])
                            self.clean_tile()
                            partition_performance -= len(min_moves) - 1
                        else:
                            print("No valid path to overcome the hurdle.")
                elif self.grid[y][x]:
                    self.clean_tile()
                    partition_performance -= 1

        print("After Cleaning:")
        self.print_grid()
        print("Performance Score:", partition_performance)
        self.total_performance += partition_performance

        print("=" * 35)

    def find_alternative_moves(self, x, y):
        possible_moves = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < self.cols and 0 <= new_y < self.rows and not self.grid[new_y][new_x] and (new_x, new_y) not in self.hurdles:
                    possible_moves.append(self.find_path_to_dirt(x, y, new_x, new_y))
        return possible_moves

    def find_path_to_dirt(self, start_x, start_y, target_x, target_y):
        visited = set()
        queue = [(start_x, start_y, [])]

        while queue:
            x, y, path = queue.pop(0)
            if (x, y) == (target_x, target_y):
                return path + [(x, y)]
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < self.cols
                    and 0 <= new_y < self.rows
                    and not self.grid[new_y][new_x]
                    and (new_x, new_y) not in self.hurdles
                ):
                    queue.append((new_x, new_y, path + [(new_x, new_y)]))
        return []

    def print_grid(self):
        for y in range(self.rows):
            row_str = ""
            for x in range(self.cols):
                if self.grid[y][x]:
                    if (x, y) in self.hurdles:
                        row_str += "H "
                    else:
                        row_str += "D "
                else:
                    row_str += "C "
            print(row_str)

    def simulate(self, num_steps):
        for step in range(num_steps):
            
            print(f"Time Step {step + 1}")
            print("\n")
            
            self.place_dirt()
            self.place_hurdles()
            self.clean_partition()
            print("=" * 35)

            print(f"Total Performance Score: {self.total_performance}")
            print("\n")
    
if __name__ == "__main__":
    rows = 4
    cols = 4
    num_steps = 10

    simulation = GridSimulation(rows, cols)
    simulation.simulate(num_steps)
