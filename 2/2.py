"""Determine which games would have been possible
if the bag had been loaded
with only 12 red cubes, 13 green cubes, and 14 blue cubes.
 What is the sum of the IDs of those games?"""

data = open("day2data.txt", "r")
lines = data.read().splitlines()


def split_input_into_list(line_to_split):
    index = line_to_split.index(":")
    string = line_to_split[index + 1:]
    return string.split(";")


def split_game_line_list_into_draw_list(game_line_list):
    split_lines = []
    for line in game_line_list:
        split_lines.append(split_game_line(line))
    return split_lines


def split_game_line(game_line):
    return game_line.strip().split(",")


def split_draw_list_into_color_dict_list(draw_line):
    draws = []
    for draw in draw_line:
        draws.append(split_draw_line_into_color_dict(draw))
    return draws


def split_draw_line_into_color_dict(draw_line):
    color_dict = {"red": 0, "green": 0, "blue": 0}
    for draw in draw_line:
        values = draw.strip().split(" ")
        amount = values[0]
        color = values[1]
        color_dict[color] = int(amount)
    return color_dict


def get_games_from_data():
    games = []
    for line in lines:
        game_line_list = split_input_into_list(line)
        draw_list = split_game_line_list_into_draw_list(game_line_list)
        games.append(split_draw_list_into_color_dict_list(draw_list))
    return games


def check_game(game):
    for draw in game:
        if not check_draw(draw):
            return False
    return True


def check_draw(draw):
    for key in configuration:
        if draw[key] > configuration[key]:
            return False
    return True


def fewest_in_game(game):
    fewest = {"red": 0, "green": 0, "blue": 0}
    for draw in game:
        for key in fewest:
            fewest[key] = max(draw[key], fewest[key])
    return fewest


def calc_power_from_fewest(fewest):
    power = 1
    for key in fewest:
        power *= fewest[key]
    return power


def get_fewest_power(game):
    fewest = fewest_in_game(game)
    return calc_power_from_fewest(fewest)


def calc_sum_of_possible_games():
    sum_of_possible_games = 0
    games = get_games_from_data()
    count = 1
    for game in games:
        if check_game(game):
            sum_of_possible_games += count
        count += 1
    return sum_of_possible_games


def calc_sum_of_power_of_games():
    games = get_games_from_data()
    sum_of_power = 0
    for game in games:
        sum_of_power += get_fewest_power(game)
    return sum_of_power


configuration = {"red": 12, "green": 13, "blue": 14}

print(calc_sum_of_possible_games())

print(calc_sum_of_power_of_games())
