from operator import itemgetter
import timeit

data = open("example2.txt", "r")
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

conns = {"s": ["|", "L", "J"],
         "n": ["|", "7", "F"],
         "w": ["-", "F", "L"],
         "e": ["-", "J", "7"]}
dirs = {"|": ["n", "s"],
        "-": ["e", "w"],
        "7": ["s", "w"],
        "F": ["s", "e"],
        "L": ["n", "e"],
        "J": ["n", "w"]}
infer_pipes = {
    "ns": "|",
    "ne": "L",
    "nw": "J",
    "sn": "|",
    "se": "F",
    "sw": "7",
    "en": "L",
    "ew": "-",
    "es": "F",
    "wn": "J",
    "ws": "7",
    "we": "-"
}

PATH = []


def get_start_and_replace_with_pipe():
    x = 0
    y = 0
    for line in lines:
        x = 0
        for c in line:
            if c == "S":
                start_pipe = infer_start_pipe((y, x))
                # print(start_pipe)
                replace_with_pipe((y, x), start_pipe)
                return y, x
            x += 1
        y += 1


def infer_start_pipe(start_pos):
    y, x = start_pos
    offsets = [(-1, 0, "n"), (1, 0, "s"), (0, 1, "e"), [0, -1, "w"]]
    directions = ""
    for offset in offsets:
        new_y = y + offset[0]
        new_x = x + offset[1]
        direction = offset[2]
        if new_y >= len(lines) or new_y < 0:
            # print("offset: ", offset)
            continue
        if new_x >= len(lines[0]) or new_x < 0:
            # print("offset: ", offset)
            continue
        pipe = lines[new_y][new_x]
        # print("direction: ", direction)
        # print("new_pipe", pipe)
        # print("conns[direction]", conns[direction])
        if pipe in conns[direction]:
            # print("added")
            directions += direction
    return infer_pipes[directions]


def replace_with_pipe(start_pos, pipe):
    y, x = start_pos
    list_string = list(lines[y])
    list_string[x] = pipe
    lines[y] = "".join(list_string)


# print(get_start_and_replace_with_pipe())

def find_pipe_loop():
    global conns
    global PATH
    global lines
    offsets = {"n": (-1, 0),
               "s": (1, 0),
               "e": (0, 1),
               "w": (0, -1)}
    direction_offsets = {"n": "s",
                         "s": "n",
                         "e": "w",
                         "w": "e"}

    start_pos = get_start_and_replace_with_pipe()
    y, x = start_pos
    prev_pipe = lines[y][x]
    direction = dirs[prev_pipe][0]
    while start_pos not in PATH:
        off_y, off_x = offsets[direction]
        y = y + off_y
        x = x + off_x
        PATH.append((y, x))
        next_pipe = lines[y][x]
        dir_one = dirs[next_pipe][0]
        dir_two = dirs[next_pipe][1]
        dir_from = direction_offsets[direction]
        direction = dir_one if dir_one != dir_from else dir_two


def find_enclosed():
    new_lines = []
    for i in range(0, len(lines)):
        line_i = [yx for yx in PATH if yx[0] == i]
        if line_i:
            line_i.sort(key=itemgetter(1))
            new_lines.append(line_i)

    enclosed = 0

    for y in range(len(lines)):
        inside = False
        for x in range(0, len(lines[y])):
            pipe = lines[y][x]
            # print("----")
            # print("y: ", y)
            # print("x: ", x)
            # print("pipe: ", pipe)
            #solution heavily inspired / taken from: https://github.com/Yarin78/advent-of-code/blob/master/src/year2023/day10.py
            if (y,x) in PATH and (pipe == "J" or pipe == "L" or pipe == "|"):
                inside = not inside
#             print("inside: ", inside)
            enclosed += (y,x) not in PATH and inside
#             print("enclosed: ", enclosed)

    return enclosed


start_time = timeit.default_timer()
find_pipe_loop()
#print(len(PATH) / 2)
#print("time: ", timeit.default_timer() - start_time)
# print("4 excepted: ", 4 == find_enclosed())
LAST_GUESS = 876
guess = find_enclosed()
print(guess)
print(guess < LAST_GUESS)



## OLD
def find_start():
    x = 0
    y = 0
    for line in lines:
        x = 0
        for c in line:
            if c == "S":
                return [(y, x)]
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
    # print("pipe coord: ", pipe_coord)
    y, x = pipe_coord
    cur_pipe = lines[y][x]
    #     # print("pipe coord: ", pipe_coord)
    #     # print("cur pipe: ", cur_pipe)
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
            #             print("pipe: ", pipe)
            #             print("direction: ", direction)
            if pipe in connections[direction_offsets[direction]]:
                y_offset = offsets[direction][0]
                x_offset = offsets[direction][1]
                add_y, add_x = y + y_offset, x + x_offset
                connections_found.append((add_y, add_x))
                # PATH.append((add_y,add_x))
        elif cur_pipe in connections[direction]:
            #             print("direction: ", direction)
            # print("elif cur pipe: ", cur_pipe)
            #             print("connections[direction] ", connections[direction])
            y_offset = offsets[direction][0]
            x_offset = offsets[direction][1]
            add_y, add_x = y + y_offset, x + x_offset
            if add_y < 0 or add_x < 0:
                # print("skip below zero")
                continue
            if add_y >= len(lines) or add_x >= len(lines[0]):
                #                 print("skip len =")
                #                 print("add_y: ", add_y)
                #                 print("add_x: ", add_x)
                continue
            if (add_y, add_x) not in PATH:
                #                 print("add to path!")
                connections_found.append((add_y, add_x))
                # print("add")
                break
    # PATH.append((add_y,add_x))
    return connections_found


def find_all():
    curr_pos = find_start()
    # print("curr pos", curr_pos)
    count = 0
    while curr_pos not in PATH:
        # print("count: ", count)
        # # print(get_connections(curr_pos))
        if len(curr_pos) > 1:
            #             print("len > 1")
            #             print("currpos: ", curr_pos)
            curr_pos = get_connections(curr_pos[0])
        else:
            curr_pos = get_connections(curr_pos[0])
        #         print(curr_pos)
        count += 1
        if not curr_pos:
            return count


#         print("cur pos: ", curr_pos)

def find_area():
    for coord in PATH:
        y, x = coord
        list_string = list(lines[y])
        list_string[x] = "P"
        lines[y] = "".join(list_string)
    for line in lines:
        print(line)


def find_edges():
    edges = []
    for i in range(len(lines)):
        edges_i = [xy for xy in PATH if xy[0] == i]
        min_x_edge = min(edges_i, key=itemgetter(1))
        max_x_edge = max(edges_i, key=itemgetter(1))
        min_max_edges = [min_x_edge, max_x_edge]
        edges.append(min_max_edges)
    return edges


def find_diff(edges):
    sum = 0
    for edge in edges:
        diff = edge[1][1] - edge[0][1]
        sum += diff
    return sum


def find_walls():
    walls = []
    for i in range(len(lines)):
        walls_i = []
        # print("path: ", PATH)
        edges_i = [yx for yx in PATH if yx[0] == i]
        edges_i = sorted(edges_i, key=itemgetter(1))
        # print("edge_i: " ,edges_i)
        if not edges_i:
            continue
        first = edges_i[0]
        last = first
        # print("i : ", i)
        # print("edges_i: ", edges_i)
        for edge in edges_i:
            #             print("edge: ", edge)
            #             print("last: ", last)
            if edge == first:
                continue
            if (last[1] + 1) == edge[1]:
                #                 print("wall building")
                last = edge
                wall = (first[1], last[1])
            else:
                # print("else: ", edge)
                wall = (first[1], last[1])
                #                 print("wall: ", wall)
                walls_i.append(wall)
                first = edge
                last = first

        #                 print(wall)
        walls_i.append(wall)
        walls.append(walls_i)
    return walls


def find_enclosed(walls):
    enclosed = 0
    top_wall = []
    i = 0
    while i < len(walls):
        start = 0
        end = 0
        print("i :", i)
        print("len walls: ", len(walls))
        for wall in walls[i]:
            print("wall: ", wall)
            print("top wall: ", top_wall)
            if not top_wall:
                print(wall)
                top_wall.append(wall)
            else:
                for tw in top_wall:
                    print("tw: ", tw)
                    tw_min_x, tw_max_x = tw
                    w_min_x, w_max_x = wall
                    if w_min_x < tw_min_x and w_max_x < tw_max_x:
                        top_wall.append(wall)
                    elif w_min_x < tw_min_x < w_max_x:
                        tw = w_min_x, tw[1]
                    elif tw_min_x < w_min_x <= tw_max_x:
                        tw = tw[0], w_max_x
                    elif w_min_x > tw_min_x and w_max_x > tw_max_x:
                        top_wall.append(wall)
                    else:
                        continue
        print("add 1")
        i += 1
    print("top wall below vvvv")
    print(top_wall)
    print("hej")

    return enclosed


#       0 1 2 3 4
#     0 # P P P #
#     1 P P # P P
#     2 P # # # P
#     3 P P # P P
#     4 # P P P #

# 1,3
# 1,3
# 1,3 1,2 1,1
# 1,1,1
# 1,1


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
# PATH = []
# start_time = timeit.default_timer()
# print(find_all()/2)
# print("time: ", timeit.default_timer() - start_time)
# edges = find_edges()
# print(find_diff(edges))

# walls = find_walls()
# print("walls: ", walls)
# print(find_enclosed(walls))
# find_area()
# print(PATH)
#find_area()
# print(len(PATH))
