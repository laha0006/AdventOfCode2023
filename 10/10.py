data = open("example.txt", "r")
lines = data.read().splitlines()

connections = {"n": {"|": ["F", "/", "|"],
                     "L": ["|", "7", "F"],
                     "J": ["|", "7", "F"]},
               "s": {"|": ["L", "J", "|"],
                     "7": ["L", "J", "|"],
                     "F": ["L", "J", "|"]},
               "e": {"-": ["7", "J", "-"],
                     "L": ["-", "J", "7"],
                     "F": ["-", "J", "7"]},
               "w": {"-": ["L", "F", "-"],
                     "J": ["-", "F", "L"],
                     "7": ["-", "F", "L"]}}

PATH = []
def find_start():
    x = 0
    y = 0
    for line in lines:
        x = 0
        for c in line:
            if c == "S":
                return y, x
            x += 1
        y += 1


def find_loop_length():
    print("implement me")


def get_connections(pipe_coord):
    if pipe_coord not in PATH:
        PATH.append(pipe_coord)
    offsets = {"n": (-1, 0),
               "s": (1, 0),
               "e": (0, 1),
               "w": (0, -1)}
    direction_offsets = {"n": "s",
                         "s": "n",
                         "e": "w",
                         "w": "e"}
    y, x = pipe_coord
    cur_pipe = lines[y][x]
    # print("pipe coord: ", pipe_coord)
    # print("cur pipe: ", cur_pipe)
    connections_found = []
    for direction in connections:
        if cur_pipe == "S":
            y_offset = offsets[direction][0]
            x_offset = offsets[direction][1]
            check_y, check_x = y + y_offset, x + x_offset
            if check_y < 0 or check_x < 0:
                continue
            if check_y >= len(lines) or check_x >= len(lines[0]):
                continue
            pipe = lines[check_y][check_x]
            print("pipe: ", pipe)
            print("direction: ", direction)
            if pipe in connections[direction_offsets[direction]]:
                y_offset = offsets[direction][0]
                x_offset = offsets[direction][1]
                add_y, add_x = y + y_offset, x + x_offset
                connections_found.append((add_y, add_x))
                #PATH.append((add_y,add_x))
        elif cur_pipe in connections[direction]:
            print("direction: ", direction)
            print("elif cur pipe: ", cur_pipe)
            print("connections[direction] ", connections[direction])
            y_offset = offsets[direction][0]
            x_offset = offsets[direction][1]
            add_y, add_x = y + y_offset, x + x_offset
            if add_y < 0 or add_x < 0:
                print("skip below zero")
                continue
            if add_y >= len(lines) or add_x >= len(lines[0]):
                print("skip len =")
                print("add_y: ", add_y)
                print("add_x: ", add_x)
                continue
            if (add_y, add_x) not in PATH:
                print("add to path!")
                connections_found.append((add_y, add_x))
                #PATH.append((add_y,add_x))
    return connections_found


def find_all():
    curr_pos = find_start()
    count = 0
    while curr_pos not in PATH:
        print("count: ", count)
        print(get_connections(curr_pos))
        curr_pos = get_connections(curr_pos)[0]
        print("cur pos: ", curr_pos)
        count += 1

# print(find_start())
# y, x = find_start()
# print(lines[y][x])

# start_connections = get_connections((y, x))
# print(start_connections)
# print(PATH)
#
# y, x = start_connections[0]
# print(get_connections((y , x)))
# print(PATH)

find_all()
# print(len(PATH))
