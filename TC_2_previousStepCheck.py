from main import VCAgent

world = [[1, 0],
         [-1, 1]]
vcagent = VCAgent(world)
vcagent.set_current(0, 0)

initial_location = vcagent.current_x, vcagent.current_y

vcagent.move(1, 1) 
vcagent.clean(1,0)

modified_world = vcagent.get_world()
print("Modified world:\n", modified_world)

previous_location = initial_location
new_location = vcagent.current_x+1, vcagent.current_y+1

print("Previous location:", previous_location)
print("New location:", new_location)

if previous_location == new_location:
    print("Previous location test failed\n")
else:
    print("Previous location test passed\n")
