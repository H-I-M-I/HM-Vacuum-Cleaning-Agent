from main import VCAgent

world = [[1, 0],
        [-1, 1]]
vcagent = VCAgent(world)
vcagent.set_current(0, 0)

vcagent.move(1, 0) 
vcagent.clean(1, 1)
modified_world = vcagent.get_world()

print("Modified world:\n", modified_world)

if(modified_world[1][0]==VCAgent.VC):
    print("\nMovement test passed\n")
else:
    print("\nMovement test failed\n")
    
