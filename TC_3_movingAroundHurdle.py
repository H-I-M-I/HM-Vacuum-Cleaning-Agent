from main import VCAgent

H = 999
world = [[0,  1,  0],
         [H,  H, -1],
         [0,  0,  0]]

vcagent = VCAgent(world)
vcagent.set_current(2, 1)

vcagent.move(-2,1)
vcagent.clean(0,1)
vcagent.clean(1,2)

modified_world = vcagent.get_world()
print("Modified world:\n", modified_world)

expected_world = [[0, 0, -1],
                  [H, H, 0],
                  [0, 0, 0]]

# expected_world = [[0 if tile == 'H' or tile == 0 or tile == 1 else tile for tile in row] for row in expected_world]

if modified_world == expected_world:
    print("Navigation and cleaning test passed\n")
else:
    print("Navigation and cleaning test failed\n")
