import random

class Environment:
    def __init__(self):
        self.width = 2
        self.height = 1
        self.grid = [random.random() < 0.3 for _ in range(self.width)]

    def is_dirty(self, x):
        return self.grid[x]

    def clean(self, x):
        self.grid[x] = False

    def print_grid(self):
        print("".join(["------- " if cell else "------- " for cell in self.grid]))
        print("".join(["|dirty| " if cell else "|clean| " for cell in self.grid]))
        print("".join(["------- " if cell else "------- " for cell in self.grid]))

class VacuumCleaner:
    def __init__(self, environment):
        self.x = random.randint(0, environment.width - 1)
        self.environment = environment

    def move_left(self):
        if self.x > 0:
            self.x -= 1

    def move_right(self):
        if self.x < self.environment.width - 1:
            self.x += 1

    def suck(self):
        if self.environment.is_dirty(self.x):
            self.environment.clean(self.x)
            return 1 
        return 0

    def get_location(self):
        return self.x

if __name__ == "__main__":
    total_score = 0
    num_configurations = 0

    for _ in range(1000):
        for x1 in [False, True]:  # Initial dirt position for tiles 1
            for x2 in [False, True]:  # Initial dirt position for tiles 2
                for agent_x in range(2):  # Agent's initial location (0 or 1)
                    environment = Environment()
                    environment.grid[0] = x1
                    environment.grid[1] = x2

                    vacuum_cleaner = VacuumCleaner(environment)
                    vacuum_cleaner.x = agent_x

                    print("\nInitial Agent Location:", vacuum_cleaner.get_location())

                    print("Initial Dirt Location:")
                    environment.print_grid()

                    performance_score = 0
                    points = 0

                    for move_num in range(1, 4):
                        move_type = random.choice(["left", "right", "suck"])

                        if move_type == "left":
                            # print(f"\nMove {move_num}: Go Left")
                            vacuum_cleaner.move_left()
                        elif move_type == "right":
                            # print(f"\nMove {move_num}: Go Right")
                            vacuum_cleaner.move_right()
                        elif move_type == "suck":
                            # print(f"\nMove {move_num}: Suck up Dirt")
                            vacuum_cleaner.suck()

                        for x in range(environment.width):
                            if environment.is_dirty(x):
                                environment.clean(x)
                                points += 1

                    print("After cleaning:")
                    environment.print_grid()
                    performance_score = points
                    print("Performance Score:", performance_score)
                    print("\n")

                total_score += performance_score
                num_configurations += 1
    
    print("Total Performance score:", total_score)
    average_score = total_score / num_configurations
    print("\nOverall Average Score:", average_score)
    print("\n")