from main import VCAgent

H = 999
world = [[1,  0, 0],
         [0, -1, H],
         [1,  H, 1]]  
vcagent = VCAgent(world)
vcagent.set_current(2, 2)

current_world = vcagent.get_world()

if vcagent.get_world()[2][1] != H:
    vcagent.move(0, -1)

modified_world = vcagent.get_world()

if modified_world == current_world:
    print("Movement not performed due to obstacle")
else:
    print("Successfully moved despite the obstacle")

vcagent.set_current(2, 2)
current_world = vcagent.get_world()

if vcagent.get_world()[1][2] != H:
    vcagent.move(-2, 0)

modified_world = vcagent.get_world()

if modified_world == current_world:
    print("Movement not performed due to obstacle")
else:
    print("Successfully moved despite the obstacle")
