import random

class GridSimulation:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[999 for _ in range(cols)] for _ in range(rows)]
        self.agent_x = random.randint(0, cols - 1)
        self.agent_y = random.randint(0, rows - 1)
        self.total_performance = 0
        self.cleaned_partitions = set()
        self.hurdles = []
        self.extra_moves = {}  

    def place_dirt(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col] = random.choice([False, True])

    def place_hurdles(self, hurdle_rate=0.125):
        num_hurdles = int(self.rows * self.cols * hurdle_rate)
        possible_locations = [(x, y) for y in range(self.rows) for x in range(self.cols)]
        
        num_extra_hurdles = int(num_hurdles * 0.125) 
        extra_hurdles = random.sample(possible_locations, num_extra_hurdles)
        
        for i in range(len(extra_hurdles) - 1):
            x1, y1 = extra_hurdles[i]
            x2, y2 = extra_hurdles[i + 1]
            if abs(x1 - x2) == 1 and y1 == y2:
                extra_hurdles.append(((x1 + x2) // 2, y1))
        
        self.hurdles = random.sample(possible_locations, num_hurdles - num_extra_hurdles) + extra_hurdles
        
        for (x, y) in self.hurdles:
            self.grid[y][x] = 999


    def clean_tile(self):
        self.grid[self.agent_y][self.agent_x] = False

    def move_agent(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
           if self.grid[y][x] != 999:
              self.agent_x = x
              self.agent_y = y
           else:
            print("Agent cannot move due to a hurdle.")
        else:
           print("Agent cannot move out of bounds.")

    def recent_cleaned(self, partition_x, partition_y):
        if (partition_x, partition_y) in self.cleaned_partitions:
            print(f"Partition ({partition_x}, {partition_y}) already cleaned. Skipping.")
            return
        
        self.cleaned_partitions.add((partition_x, partition_y))

    def clean_partition(self, partition_x, partition_y):
        
        start_x = partition_x * 2
        start_y = partition_y * 2
        
        print(f"Partition ({partition_x}, {partition_y}):")
        print("Before Cleaning:")
        movements = []
        self.print_partition(start_x, start_y)
        cleaned_count = 4 - sum(1 for y in range(start_y, start_y + 2) for x in range(start_x, start_x + 2) if self.grid[y][x])
        
        hurdles_encountered = []
        extra_moves_info = {}
        
        for y in range(start_y, start_y + 2):
            for x in range(start_x, start_x + 2):
                self.agent_x = x
                self.agent_y = y
                movements.append((x, y))  
                if (x, y) in self.hurdles:
                    hurdles_encountered.append((x, y)) 
                    extra_moves_info[(x, y)] = self.extra_moves.get((x, y), 0) + 1
                elif self.grid[y][x]:
                    self.clean_tile()

        print("Movements:", movements)
        print("After Cleaning:")
        self.print_partition(start_x, start_y)
        self.total_performance += cleaned_count

        print("Hurdles Encountered:", hurdles_encountered)
        print("Extra Moves for Each Tile:", extra_moves_info)
        print("Performance Score:", cleaned_count)
        print("Total Performance Score:", self.total_performance)
        
        new_partition_x = random.choice([0, 1])
        new_partition_y = random.choice([0, 1])
        while new_partition_x == partition_x and new_partition_y == partition_y:
            new_partition_x = random.choice([0, 1])
            new_partition_y = random.choice([0, 1])
        
        new_agent_x = new_partition_x * 2 + random.choice([0, 1])
        new_agent_y = new_partition_y * 2 + random.choice([0, 1])
        
        self.move_agent(new_agent_x, new_agent_y)
        print(f"New Agent Position: ({new_agent_x}, {new_agent_y})")
        print("=" * 25)


    def print_partition(self, start_x, start_y):
        for y in range(start_y, start_y + 2):
            row_str = ""
            for x in range(start_x, start_x + 2):
                if self.grid[y][x]:
                    row_str += "D "
                else:
                    row_str += "C "
            print(row_str)

    def simulate(self, num_steps):
        for step in range(num_steps):
            print(f"Time Step {step + 1}")
            self.place_dirt()
            
            for partition_y in range(2):
                for partition_x in range(2):
                    self.clean_partition(partition_x, partition_y)
                    print("=" * 25)

if __name__ == "__main__":
    rows = 4
    cols = 4
    num_steps = 1000

    simulation = GridSimulation(rows, cols)
    simulation.place_hurdles()
    simulation.simulate(num_steps)
