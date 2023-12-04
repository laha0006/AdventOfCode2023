# gets a list of string digits "1","2"..."9".
# where "one" "two" ... "nine" is also transformed to a string digit
def get_list_of_string_digits_from_string(string):
    word_digits_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                        "eight": "8", "nine": "9"}
    digits = []
    i = 0
    while i < len(string):
        five_char_word_digit = string[i:i + 5]
        four_char_word_digit = string[i:i + 4]
        three_char_word_digit = string[i:i + 3]
        char = string[i]
        if five_char_word_digit in word_digits_dict:
            digits.append(word_digits_dict[five_char_word_digit])
            i += 4
        elif four_char_word_digit in word_digits_dict:
            digits.append(word_digits_dict[four_char_word_digit])
            i += 3
        elif three_char_word_digit in word_digits_dict:
            digits.append(word_digits_dict[three_char_word_digit])
            i += 2
        elif char.isnumeric():
            digits.append(char)
            i += 1
        else:
            i += 1

    return digits


def get_two_digit_number_from_first_and_last_string_digit_in_list(string_digit_list):
    return int(string_digit_list[0]+string_digit_list[-1])


def calc_calibration_value(string):
    digit_list = get_list_of_string_digits_from_string(string)
    return get_two_digit_number_from_first_and_last_string_digit_in_list(digit_list)


def calc_sum_of_calibration_values(list_of_lines):
    sum_of_calibration_values = 0
    for s in list_of_lines:
        num = calc_calibration_value(s)
        sum_of_calibration_values += num
    return sum_of_calibration_values


day_one_data = open("day1data.txt", "r")
lines = day_one_data.read().splitlines()

print(calc_sum_of_calibration_values(lines))

