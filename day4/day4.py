# CHALLENGE INTRO:
#


def get_lesser_start(secs1, secs2):
    secs1_split = secs1.split("-")
    secs2_split = secs2.split("-")
    for i in range(2):
        secs1_split[i] = int(secs1_split[i])
        secs2_split[i] = int(secs2_split[i])
    if secs1_split[0] < secs2_split[0]:
        return secs1
    if secs1_split[0] == secs2_split[0]:
        secs1_len = secs1_split[-1] - secs1_split[0]
        secs2_len = secs2_split[-1] - secs2_split[0]
        if secs1_len > secs2_len:
            return secs1
    return secs2


def get_greater_end(secs1, secs2):
    secs1_split = secs1.split("-")
    secs2_split = secs2.split("-")
    for i in range(2):
        secs1_split[i] = int(secs1_split[i])
        secs2_split[i] = int(secs2_split[i])
    if secs1_split[-1] > secs2_split[-1]:
        return secs1
    if secs1_split[0] == secs2_split[0]:
        secs1_len = secs1_split[-1] - secs1_split[0]
        secs2_len = secs2_split[-1] - secs2_split[0]
        if secs1_len > secs2_len:
            return secs1
    return secs2


def fully_contains(assn_pair):
    assn_pair = assn_pair.split(",")
    secs1 = assn_pair[0]
    secs2 = assn_pair[1]
    if secs1 == secs2:
        return True
    test1 = get_lesser_start(secs1, secs2)
    test2 = get_greater_end(secs1, secs2)
    if test1 == test2:
        return True
    return False


num_containing_pairs = 0
with open("./day4/day4_input.txt") as pairs_list:
    assn_pair = pairs_list.readline().strip()
    while assn_pair != "":
        if fully_contains(assn_pair):
            num_containing_pairs += 1
            print(assn_pair)
        assn_pair = pairs_list.readline().strip()
print(num_containing_pairs, end=" ")
print("pairs have one range that fully contains the other")
