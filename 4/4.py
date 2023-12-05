data = open("day4data.txt", "r")
lines = data.read().splitlines()


def split_input_into_list(line_to_split):
    index = line_to_split.index(":")
    string = line_to_split[index + 1:]
    return string.split("|")


def split_line_into_winning_and_gotten_numbers(line_to_split):
    return_card = []
    # print(line_to_split)
    for line in line_to_split:
        card = line.rstrip().lstrip().split(" ")
        temp = []
        for num in card:
            if num.isnumeric():
                temp.append(num)
        card = temp
        return_card.append(card)
    return return_card


def scrub_input_into_list(lines_to_scrub):
    return_lines = []
    count = 0
    for line in lines_to_scrub:
        raw_card = split_input_into_list(line)
        card_numbers = split_line_into_winning_and_gotten_numbers(raw_card)
        card = {"ID": count, "numbers": card_numbers}
        return_lines.append(card)
        count += 1
    #print("count of cards: ", count)
    return return_lines


def score_of_card(card):
    winning = card[0]
    gotten = card[1]

    winners = 0
    score = 0

    for num in gotten:
        if num in winning:
            if winners == 0:
                score += 1
                winners += 1
            else:
                score *= 2
                winners += 1
    return score


def get_won_cards_from_card(card):
    won_cards = []
    winning = card["numbers"][0]
    gotten = card["numbers"][1]
    num_won_cards = card["ID"]

    for num in gotten:
        if num in winning:
            # say we have card 207 with 4 winners.
            # 208,209,210. stop.
            num_won_cards += 1
            won_card = min(num_won_cards, 210)
            #print("won card:", won_card)
            if won_card != card["ID"] or won_card not in won_cards:
                won_cards.append(won_card)
            else:
                return won_cards
    return won_cards


def calc_sum_of_wining_cards(lines_to_use):
    cards = scrub_input_into_list(lines_to_use)
    total_score = 0
    for card in cards:
        score = score_of_card(card)
        total_score += score
    return total_score


def get_copy_of_won_cards(won_cards, original_cards):
    copies = []
    #print("won_cards", won_cards)
    for card in won_cards:
        copies.append(original_cards[card].copy())
    return copies


def calc_num_of_cards(lines_to_use):
    cards = scrub_input_into_list(lines_to_use)
    cards_to_process = cards.copy().copy()
    count = 0
    for card in cards_to_process:
        #print("count: ", count )
        # print("process len: ", len(cards_to_process)-count)
        #print("card: ", card)
        won_cards = get_won_cards_from_card(card)
        copy_cards = get_copy_of_won_cards(won_cards, cards)
        # print("copies: ", copy_cards)
        cards_to_process.extend(copy_cards)

        count += 1
    return count


# print(calc_sum_of_wining_cards(lines))
print(calc_num_of_cards(lines))
