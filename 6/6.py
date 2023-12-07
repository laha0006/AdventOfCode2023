data = open("day6data.txt", "r")
lines = data.read().splitlines()

_, rest = lines[0].split(":")
TIME = [int(x) for x in rest.split()]
ONE_TIME = int(rest.strip().replace(" ", ""))
print("ONE_TIME ", ONE_TIME)
_, rest = lines[1].split(":")
DIST = [int(x) for x in rest.split()]
ONE_DIST = int(rest.strip().replace(" ", ""))
print("ONE_DIST ", ONE_DIST)

def calc_num_win_strats(race):
    time = TIME[race]
    dist = DIST[race]

    win = 0
    for i in range(time+1):
        speed = i
        time_left = time - i
        dist_travelled = speed * time_left
        if dist_travelled >= dist:
            win += 1
    return win


# A = 1
# for i in range(len(TIME)):
#     A *= calc_num_win_strats(i)
# print(A)

t = 10


def g(x):
    print(f'x: {x}, (t- x): {t- x},(x * (t - x)): {x * (t - x)} ')
    return x * (t - x)


def calc_num_binary_test():
    time = 100
    dist = 2500

    win = 0
    for i in range(time + 1):
        speed = i
        time_left = time - i
        dist_travelled = speed * time_left
        print("speed: ", speed)
        print("dist_travveled: ", dist_travelled)
        if dist_travelled >= dist:
            win += 1
    return win


def calc_num_one_race():
    time = ONE_TIME
    dist = ONE_DIST

    win = 0
    for i in range(time + 1):
        speed = i
        time_left = time - i
        dist_travelled = speed * time_left
        if dist_travelled >= dist:
            win += 1
    return win

g(1)
g(2)
g(3)
g(4)
g(5)
g(6)
g(7)
g(8)
g(9)
g(10)
#print(calc_num_binary_test())


print(g(5))
print(g(10-5))