data = open("day3data.txt", "r")
lines = data.read().splitlines()

schematic = lines
one_line = [
    "48.................501....33.....622..............763.........331.................161.683......................................980.........."]
s = "...491.842.....948*..................338.....*......=...........-...309.......633*....*....................*990...706...452......*..+......."

example_data = open("example.txt", "r")
example_lines_input = example_data.read()


# [[(0,0),(0,1)], [(0,19),(0,20),(0,21)] ]
def get_list_of_numbers_represented_as_list_of_tuples_of_coordinates(lines_input):
    numbers = []
    number = []
    line_count = 0
    for line in lines_input:
        number_found = False
        char_count = 0
        for c in line:
            if c.isnumeric() and not number_found:
                number.append((line_count, char_count))
                char_count += 1
                number_found = True
            elif c.isnumeric() and number_found:
                number.append((line_count, char_count))
                char_count += 1
            elif not c.isnumeric() and number_found:
                numbers.append(number.copy())
                number.clear()
                number_found = False
                char_count += 1
            else:
                char_count += 1
        if number_found:
            numbers.append(number.copy())
            number.clear()
        line_count += 1
    return numbers


def check_adj_symbol_number(number):
    for digit in number:
        if check_adj_symbol_digit(digit):
            print(number)
            return True
    return False


def check_adj_symbol_digit(digit):
    offsets_x = [-1, 0, 1, -1, 1, -1, 0, 1]
    offsets_y = [1, 1, 1, 0, 0, -1, -1, -1]
    for x in range(len(offsets_x)):
        for y in range(len(offsets_y)):
            offset_x = min(max((offsets_x[x] + digit[1]), 0), 139)
            offset_y = min(max((offsets_y[y] + digit[0]), 0), 139)
            adj = lines_input[offset_y][offset_x]
            if not adj.isnumeric() and adj != ".":
                # print("adj: ", adj)
                return True
    return False


def number_list_to_number(number):
    number_string = ""
    for i in number:
        number_string += str(lines[i[0]][i[1]])
    return int(number_string)


def get_list_of_numbers_with_symbol_adj():
    raw_numbers = get_list_of_numbers_represented_as_list_of_tuples_of_coordinates()
    numbers = []
    for number in raw_numbers:
        if check_adj_symbol_number(number):
            numbers.append(number_list_to_number(number))
    return numbers


def get_list_stars():
    stars = []
    line_count = 0
    for line in lines:
        char_count = 0
        for c in line:
            if c == "*":
                stars.append((line_count, char_count))
                char_count += 1
            else:
                char_count += 1
        line_count += 1
    return stars


def get_stars_with_exact_two_numbers_adj(stars):
    exact_stars = []
    count = 0
    for star in stars:
        if exact_two_numbers_adj(star):
            print("adj!")
            exact_stars.append(star)
        count += 1
    return exact_stars


def exact_two_numbers_adj(star):
    adj_count = 0
    used_numbers = []

    offsets_x = [-1, 0, 1, -1, 1, -1, 0, 1]
    offsets_y = [1, 1, 1, 0, 0, -1, -1, -1]

    for x in range(len(offsets_x)):
        for y in range(len(offsets_y)):
            offset_x = min(max((offsets_x[x] + star[1]), 0), 139)
            offset_y = min(max((offsets_y[y] + star[0]), 0), 139)
            adj = (offset_y, offset_x)
            for number in GLOBAL_NUMBERS:
                if check_if_star_adj_to_number(adj, number) and number not in used_numbers:
                    adj_count += 1
                    used_numbers.append(number)
    return adj_count == 2


def check_if_star_adj_to_number(adj, number):
    if adj in number:
        return True
    return False


def calc_sum_of_part_numbers():
    numbers = get_list_of_numbers_with_symbol_adj()
    sum_of_part_numbers = 0
    for number in numbers:
        sum_of_part_numbers += number
    return sum_of_part_numbers


def get_two_numbers_from_star(star):
    offsets_x = [-1, 0, 1, -1, 1, -1, 0, 1]
    offsets_y = [1, 1, 1, 0, 0, -1, -1, -1]
    used_numbers = []

    two_numbers = []
    for x in range(len(offsets_x)):
        for y in range(len(offsets_y)):
            offset_x = min(max((offsets_x[x] + star[1]), 0), 139)
            offset_y = min(max((offsets_y[y] + star[0]), 0), 139)
            adj = (offset_y, offset_x)
            for number in GLOBAL_NUMBERS:
                if check_if_star_adj_to_number(adj, number) and number not in used_numbers:
                    two_numbers.append(number)
                    used_numbers.append(number)
    # print("len two numbers: ", len(two_numbers))
    return two_numbers


def calc_power_from_star(star):
    two_numbers = get_two_numbers_from_star(star)
    num_sum = 1
    for number in two_numbers:
        num = number_list_to_number(number)
        num_sum *= num
    return num_sum


def calc_sum_gear_ratio_power():
    stars_list = get_list_stars()
    print("star_list", len(stars_list))
    exact_stars = get_stars_with_exact_two_numbers_adj(stars_list)
    print("exact_list", len(exact_stars))
    sum_power = 0
    for star in exact_stars:
        power = calc_power_from_star(star)
        sum_power += power
    return sum_power


GLOBAL_NUMBERS = get_list_of_numbers_represented_as_list_of_tuples_of_coordinates(lines)

# print(calc_sum_of_part_numbers())
print("result: ", calc_sum_gear_ratio_power())
