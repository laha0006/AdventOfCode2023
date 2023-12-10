from collections import defaultdict
from functools import cmp_to_key

data = open("day7data.txt", "r")
lines = data.read().splitlines()
hands_bids = [line.split() for line in lines]

print("day 7!")

card_values = {"A": 13, "K": 12,
               "Q": 11, "J": 0,
               "T": 9, "9": 8, "8": 7,
               "7": 6, "6": 5, "5": 4,
               "4": 3, "3": 2, "2": 1}
hand_values = {"Five of a kind": 6,
               "Four of a kind": 5,
               "Full house": 4,
               "Three of a kind": 3,
               "Two pairs": 2,
               "One pair": 1}


def promote(hand):
    hand = hand.replace("J", "")
    j_count = 5 - len(hand)
    card_dict = defaultdict(int)
    amount_dict = defaultdict(int)
    for c in hand:
        card_dict[c] += 1

    for v in card_dict.values():
        amount_dict[v] += 1

    if amount_dict[5] == 1:
        return hand_values["Five of a kind"]
    elif amount_dict[4] == 1:
        return hand_values["Five of a kind"]
    elif amount_dict[3] == 1 and j_count == 2:
        return hand_values["Five of a kind"]
    elif amount_dict[3] == 1 and j_count == 1:
        return hand_values["Four of a kind"]
    elif amount_dict[2] == 2:
        return hand_values["Full house"]
    elif amount_dict[2] == 1:
        match j_count:
            case 1:
                return hand_values["Three of a kind"]
            case 2:
                return hand_values["Four of a kind"]
            case 3:
                return hand_values["Five of a kind"]
    else:
        match j_count:
            case 1:
                return hand_values["One pair"]
            case 2:
                return hand_values["Three of a kind"]
            case 3:
                return hand_values["Four of a kind"]
            case 4:
                return hand_values["Five of a kind"]
            case 5:
                return hand_values["Five of a kind"]
        return 0


def calc_hand_value(hand):
    if "J" in hand:
        return promote(hand)
    ###TODO look up cleaner solution from: https://youtu.be/22IrAlrWqu4
    # hand = hand.replace("T", chr(ord('9') + 1))
    # hand = hand.replace("J", chr(ord('9') + 2))
    # hand = hand.replace("Q", chr(ord('9') + 3))
    # hand = hand.replace("K", chr(ord('9') + 4))
    # hand = hand.replace("A", chr(ord('9') + 5))
    card_dict = defaultdict(int)
    card_value = 0
    amount_dict = defaultdict(int)
    for c in hand:
        card_dict[c] += 1
        # card_value += card_values[c]
    for v in card_dict.values():
        amount_dict[v] += 1

    if amount_dict[5] == 1:
        return hand_values["Five of a kind"]
    elif amount_dict[4] == 1:
        return hand_values["Four of a kind"]
    elif amount_dict[3] == 1 and amount_dict[2] == 1:
        return hand_values["Full house"]
    elif amount_dict[3] == 1 and amount_dict[2] == 0:
        return hand_values["Three of a kind"]
    elif amount_dict[2] == 2:
        return hand_values["Two pairs"]
    elif amount_dict[2] == 1 and amount_dict[3] == 0:
        return hand_values["One pair"]
    else:
        return 0


def tie_break(hand1, hand2):
    for i in range(5):
        c1 = card_values[hand1[0][i]]
        c2 = card_values[hand2[0][i]]
        if c1 < c2:
            return -1
        elif c1 > c2:
            return 1
    return 0


def compare(hand1, hand2):
    h1_val = calc_hand_value(hand1[0])
    h2_val = calc_hand_value(hand2[0])

    if h1_val < h2_val:
        return -1
    elif h1_val > h2_val:
        return 1
    else:
        return tie_break(hand1, hand2)


def calc_total_winnings():
    hands_bids_sorted = sorted(hands_bids, key=cmp_to_key(compare))
    rank = 1
    winnings = 0
    for hand, bid in hands_bids_sorted:
        # print("hand value: ", calc_hand_value(hand))
        win = int(bid) * rank
        winnings += win
        rank += 1
    return winnings


total = calc_total_winnings()
print(total)
# print(total != 246458924)

# print("MAX J:", MAX_J)
# print("Else: ", PROMOTE_COUNT)
# print(promote("KTJJT"))
# print(compare("JJAAA","AAAJJ"))


# def f(hand):
#     result = hand.replace("T", chr(ord('9') + 1))
#     result = result.replace("J", chr(ord('9') + 2))
#     result = result.replace("Q", chr(ord('9') + 3))
#     result = result.replace("K", chr(ord('9') + 4))
#     result = result.replace("A", chr(ord('9') + 5))
#     return result
#
#
# test1 = "AAATT"
# test2 = "KKKTT"
# test3 = "999TT"
# test4 = "777TT"
#
# test_list = [test4, test2, test1, test3]
# print(test_list)
# test_list = sorted(test_list, key=lambda x: calc_hand_value(x))
# print(test_list)
# # print(f(test1))
# # print(f(test2))
# # print(f(test3))
# # print(f(test4))

def test():
    return 1,2
print(type(test()))
