from collections import defaultdict
from math import lcm

data = open("day8data.txt", "r")
lines = data.read().splitlines()

instructions = lines[0]
instructions = instructions.replace("L", "0").replace("R", "1")
lines = lines[2:]
# start = lines[0:1][0].split("=")[0].replace(" ","")
nodes = {}
starts = []
ends = []
for line in lines:
    node, adj = line.split("=")
    node = node.strip().replace(" ", "")
    if node[2:3] == "A":
        starts.append(node)
    if node[2:3] == "Z":
        ends.append(node)
    adj = tuple(adj.strip().replace("(", "").replace(")", "").replace(" ", "").split(","))
    nodes[node] = adj

start = "AAA"


def traverse_list_nodes(runTwice):
    global starts
    global ends
    steps = []
    for i in range(len(starts)):
        step = 0
        curr_node = starts[i]
        target = ends[i]
        while not curr_node.endswith("Z"):
            move = int(instructions[step % len(instructions)])
            curr_node = nodes[curr_node][move]
            step += 1
        steps.append(step)
    return steps

def loop_test(og):
    curr_node = og
    step = 0
    found = False
    first_steps = 0
    loop_steps = 0
    while True:
        move = int(instructions[step % len(instructions)])
        curr_node = nodes[curr_node][move]
        step += 1
        if found:
            if curr_node.endswith("Z"):
                print("loop steps: ", step)
                print("node: ", curr_node)
                loop_steps = step
                break
        if curr_node.endswith("Z"):
            found = True
            first_steps = step
            print("Found steps: ", step)
            print("node:", nodes[curr_node])

    return first_steps == (loop_steps-first_steps)


def traverse_nodes(target):
    curr_node = start
    print("curr_node", curr_node)
    print("target: ", target)
    step = 0
    step_dict = defaultdict(int)
    len_inst = len(instructions)
    while curr_node != target:
        move = int(instructions[step % len(instructions)])
        curr_node = nodes[curr_node][move]
        step += 1
    return step


# print(traverse_nodes("ZZZ"))
#since they loop, we can find lcm.
#print(loop_test("AAA"))
# steps = traverse_list_nodes()
# print(lcm(steps[0], steps[1], steps[2], steps[3], steps[4], steps[5], ))


# 4 steps
# A
# 1,2,3,4
# 2,3,4,1 1 step
# 3,4,1,2 2 step
# 4,1,2,3  3 step

# B
# 4,3,2,1
#



# print(ends)
#
# test_one = ["AAB","ABB","CDC"]
# test_two = ["ABB","CDC","AAB"]
# print(test_one.sort() == test_two.sort())
