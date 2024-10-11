from main import VCAgent

H = 999
world = [[1, 0, 0, 0],
         [1, H, 0, 0],
         [1, 0, H, 0],
         [0, 0, 0, -1]]

vcagent = VCAgent(world)
vcagent.set_current(2, 3) 

target_x, target_y = -1, -1
for x in range(len(world)):
    for y in range(len(world[0])):
        if world[x][y] == 1:
            target_x, target_y = x, y
            break

shortest_path = []

while vcagent.current_x != target_x or vcagent.current_y != target_y:
    if vcagent.current_x + 1 < len(world) and vcagent.get_world()[vcagent.current_x + 1][vcagent.current_y] != H:
        vcagent.move(1, 0)
        shortest_path.append((vcagent.current_x, vcagent.current_y))
    elif vcagent.current_y + 1 < len(world[0]) and vcagent.get_world()[vcagent.current_x][vcagent.current_y + 1] != H:
        vcagent.move(0, 1)
        shortest_path.append((vcagent.current_x, vcagent.current_y))

modified_world = vcagent.get_world()

print("Shortest path:", shortest_path)
print("Modified world:\n", modified_world)
