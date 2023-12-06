from operator import itemgetter

data = open("day5data.txt", "r")
lines = data.read().splitlines()
text, seeds = lines[0].split(":")
SEEDS = [int(x) for x in seeds.split()]
lines = [line for line in lines[1:] if line]


def create_list_of_data():
    maps = []
    map = []
    for line in lines[1:]:
        if line[0].isnumeric():
            nums = [int(x) for x in line.split()]
            map.append(nums)
        else:
            maps.append(map.copy())
            map.clear()
    maps.append(map.copy())
    map.clear()
    return maps


# list_of_data = create_list_of_data()


def create_maps():
    maps = []
    count = 1
    for list_data in list_of_data:
        print("Creating map: ", count)
        maps.append(create_map(list_data))
        count += 1
    return maps


def create_map(list):
    map = {}
    for map_data in list:
        map.update(get_map_from_list(map_data))
    return map


def get_map_from_list(list):
    map = {}
    dest, source, range_num = list
    for i in range(range_num):
        map[source] = dest
        dest += 1
        source += 1
    return map


(seed_to_soil,
 soil_to_fertilizer,
 fertilizer_to_water,
 water_to_light,
 light_to_temp,
 temp_to_humidity,
 humidity_to_location) = create_list_of_data()  # create_maps()
print("created lists!")


def lookup_map(num, map):
    for line in map:
        dest, source, range_num = line
        if source <= num <= (source + range_num - 1):
            diff = num - source
            return dest + diff
    return num


def lookup_location(seed):
    soil = lookup_map(seed, seed_to_soil)
    fertilizer = lookup_map(soil, soil_to_fertilizer)
    water = lookup_map(fertilizer, fertilizer_to_water)
    light = lookup_map(water, water_to_light)
    temp = lookup_map(light, light_to_temp)
    humidity = lookup_map(temp, temp_to_humidity)
    location = lookup_map(humidity, humidity_to_location)
    return location


def lookup_map_reverse(num, map):
    for line in map:
        source, dest, range_num = line
        if source <= num <= (source + range_num - 1):
            diff = num - source
            return dest + diff
    return num


def lookup_seed_from_location(location):
    humidity = lookup_map_reverse(location, humidity_to_location)
    temp = lookup_map_reverse(humidity, temp_to_humidity)
    light = lookup_map_reverse(temp, light_to_temp)
    water = lookup_map_reverse(light, water_to_light)
    fertilizer = lookup_map_reverse(water, fertilizer_to_water)
    soil = lookup_map_reverse(fertilizer, soil_to_fertilizer)
    seed = lookup_map_reverse(soil, seed_to_soil)
    return seed


def check_if_seed(seed):
    pair_one = SEEDS[::2]
    pair_two = SEEDS[1::2]
    pairs = zip(pair_one, pair_two)

    for pair in pairs:
        start, end = pair
        if start <= seed <= start + end - 1:
            return True
    return False


def find_lowest_location():
    for location in humidity_to_location:
        loc, dest, range_num = location
        for i in range(loc + range_num):
            loc_to_check = loc + i
            seed = lookup_seed_from_location(loc_to_check)
            if check_if_seed(seed):
                return loc_to_check
    print("???")


def list_of_locations(seeds):
    locations = []
    progress = 0
    for seed in seeds:
        locations.append(lookup_location(seed))
        if progress % 100_000_000:
            print("progress: ", progress)
        progress += 1
    return locations


def get_seeds_with_ranges():
    pair_one = SEEDS[::2]
    pair_two = SEEDS[1::2]
    pairs = zip(pair_one, pair_two)

    return_seeds = []
    count = 1
    for pair in pairs:
        seed, range_num = pair
        print("# ", count)
        print(pair)
        progress = 0
        for i in range(range_num):
            seed_number = seed + i
            return_seeds.append(seed_number)
            if i % 10000000 == 0:
                print("# ", progress)
                progress += 1
        count += 1
    print("hi")
    return return_seeds


# seeds_with_ranges = get_seeds_with_ranges()
humidity_to_location = sorted(humidity_to_location, key=itemgetter(0))
print(find_lowest_location())
# print("SEEDS: ", SEEDS)
