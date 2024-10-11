class VCAgent:
    VC = -1
    CLEAN = 0
    H = 999
    
    def __init__(self, world):
        self.current_x = 1
        self.current_y = 1
        self.world = world
    
    def set_current(self, x, y):
        self.current_x = x
        self.current_y = y
    
    def move(self, dx, dy):
        self.world[self.current_x][self.current_y] = VCAgent.CLEAN
        self.world[self.current_x + dx][self.current_y + dy] = VCAgent.VC
    
    def clean(self, x, y):
        self.world[x][y] = VCAgent.CLEAN
    
    def get_world(self):
        return self.world

if __name__ == "__main__":
    world = [[1, 0],
             [-1, 1]]
    vcagent = VCAgent(world)

    clean_tiles = [[0, 0], [0, 1], [1, 1]]

    for tile in clean_tiles:
        vcagent.clean(tile[0], tile[1])
        print("Updated world:\n", vcagent.world)
