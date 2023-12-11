data = open("day9data.txt", "r")
lines = data.read().splitlines()

histories = [[int(x) for x in history] for history in [line.split() for line in lines]]


# histories = [line.split() for line in lines]
# histories = [[int(x) for x in history] for history in histories]


def next_number(history):
    sequences = get_sequences(history)
    num = 0
    i = 1
    list_len = (len(sequences) - 1)
    while list_len >= i:
        seq_above = sequences[-(i + 1)]
        num_left = seq_above[-1]
        num = num_left + num
        i += 1
    return num + history[-1]


def prev_number(history):
    sequences = get_sequences(history)
    num = 0
    i = 0
    list_len = len(sequences) - 1
    while i < list_len:
        seq_above = sequences[-(i + 2)]
        num_left = seq_above[0]
        num = num_left - num
        i += 1
    return history[0] - num


def get_sequences(history):
    seq = []
    curr_seq = history
    while not all(x == 0 for x in curr_seq):
        curr_seq = diff_list(curr_seq)
        seq.append(curr_seq)
    return seq


def diff_list(num_list):
    diff = []
    i = 0
    while i < len(num_list) - 1:
        diff.append(num_list[i + 1] - num_list[i])
        i += 1
    return diff


sum_next = 0
sum_prev = 0
for history in histories:
    next = next_number(history)
    sum_next += next
    prev = prev_number(history)
    sum_prev += prev
print(sum_next)
print(sum_prev)
