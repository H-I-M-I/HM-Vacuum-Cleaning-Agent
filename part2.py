import random

class GridSimulation:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[False for _ in range(cols)] for _ in range(rows)]
        self.agent_x = random.randint(0, cols - 1)
        self.agent_y = random.randint(0, rows - 1)
        self.total_performance = 0

    def place_dirt(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col] = random.choice([False, True])
    
    def clean_tile(self):
        self.grid[self.agent_y][self.agent_x] = False

    def move_agent(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.agent_x = x
            self.agent_y = y
        else:
            print("Agent cannot move out of bounds.")

    def clean_partition(self, partition_x, partition_y):
        start_x = partition_x * 2
        start_y = partition_y * 2
        
        print(f"Partition ({partition_x}, {partition_y}):")
        print("Before Cleaning:")
        self.print_partition(start_x, start_y)

        cleaned_count = 4 - sum(1 for y in range(start_y, start_y + 2) for x in range(start_x, start_x + 2) if self.grid[y][x])
        self.total_performance += cleaned_count
        
        for y in range(start_y, start_y + 2):
            for x in range(start_x, start_x + 2):
                self.agent_x = x
                self.agent_y = y
                self.clean_tile()

        print("After Cleaning:")
        self.print_partition(start_x, start_y)

        # Select a new partition to move the agent
        new_partition_x = random.choice([0, 1])
        new_partition_y = random.choice([0, 1])

        while new_partition_x == partition_x and new_partition_y == partition_y:
            new_partition_x = random.choice([0, 1])
            new_partition_y = random.choice([0, 1])

        # Calculate the new agent position
        new_agent_x = new_partition_x * 2 + random.choice([0, 1])
        new_agent_y = new_partition_y * 2 + random.choice([0, 1])

        self.move_agent(new_agent_x, new_agent_y)

        print("Performance Score:", cleaned_count)
        print("Total Performance Score:", self.total_performance)
        print(f"New Agent Position: ({new_agent_x}, {new_agent_y})")
        print("=" * 20)

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
                    print("=" * 20)

if __name__ == "__main__":
    rows = 4
    cols = 4
    num_steps = 1000

    simulation = GridSimulation(rows, cols)
    simulation.simulate(num_steps)
