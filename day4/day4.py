# CHALLENGE INTRO:
# The file day4_input.txt contains a pair of numerical ranges on
# each line.
#
# PART 1:
# Determine the number of pairs in which one range fully contains
# the other.
#
# PART 2:
# Determine the number of pairs in which the ranges overlap.


def lesser_start(secs1_split, secs2_split):
    """
    Determines if first number in the first range is the lesser value.

    Args
    ----
    secs1_split, secs2_split: iterables containing endpoints of range

    Returns
    -------
    True if range represented by first arg has the lesser starting
    value, False otherwise

    Raises
    ------
    TypeError: args are not iterables
    TypeError: args contain non-numerical elements
    IndexError: args contain no elements
    """
    if secs1_split[0] < secs2_split[0]:
        return True
    if secs1_split[0] == secs2_split[0]:
        secs1_len = secs1_split[-1] - secs1_split[0]
        secs2_len = secs2_split[-1] - secs2_split[0]
        if secs1_len > secs2_len:
            return True
    return False


def greater_end(secs1_split, secs2_split):
    """
    Determines if last number in the first range is the greater value.

    Args
    ----
    secs1_split, secs2_split: iterables containing endpoints of range

    Returns
    -------
    True if range represented by first arg has the greater ending
    value, False otherwise

    Raises
    ------
    TypeError: args are not iterables
    TypeError: args contain non-numerical elements
    IndexError: args contain no elements
    """
    if secs1_split[-1] > secs2_split[-1]:
        return True
    if secs1_split[-1] == secs2_split[-1]:
        secs1_len = secs1_split[-1] - secs1_split[0]
        secs2_len = secs2_split[-1] - secs2_split[0]
        if secs1_len > secs2_len:
            return True
    return False


def get_extreme_secs(secs1, secs2, mode="lesser"):
    """
    Returns given range with lesser start or greater end.

    Args
    ----
    secs1, secs2: hyphenated strings representing numerical ranges
    mode: string indicating which extreme to evaluate; can be "greater"
    or "lesser"; assigned "lesser" by default and when provided arg
    is not "greater" or "lesser"

    Returns
    -------
    provided string arg meeting condition specified by mode

    Raises
    ------
    ValueError: args do not contain int endpoints
    IndexError: args do not represent ranges with "-" char
    """
    secs1_split = secs1.split("-")
    secs2_split = secs2.split("-")
    for i in range(2):
        secs1_split[i] = int(secs1_split[i])
        secs2_split[i] = int(secs2_split[i])
    if mode == "greater" and greater_end(secs1_split, secs2_split):
        return secs1
    if mode != "greater" and lesser_start(secs1_split, secs2_split):
        return secs1
    return secs2


def get_secs(assn_pair):
    """
    Splits a pair of ranges into two strings.

    Args
    ----
    assn_pair: string containing two ranges separated by ","

    Returns
    -------
    tuple of two strings each representing numerical ranges

    Raises
    ------
    AttributeError: non-string arg provided
    IndexError: arg does not have ","
    """
    assn_pair = assn_pair.split(",")
    return (assn_pair[0], assn_pair[1])


def fully_contains(assn_pair):
    """
    Determines if one range in given pair fully contains the other.

    Args
    ----
    assn_pair: string containing two ranges separated by ","

    Returns
    -------
    True if one range fully contains the other, False otherwise

    Raises
    ------
    AttributeError: non-string arg provided
    IndexError: arg does not have ","
    """
    secs1, secs2 = get_secs(assn_pair)
    if secs1 == secs2:
        return True
    test1 = get_extreme_secs(secs1, secs2, "lesser")
    test2 = get_extreme_secs(secs1, secs2, "greater")
    return test1 == test2


def overlaps(assn_pair):
    """
    Determines if ranges in given pair overlap.

    Args
    ----
    assn_pair: string containing two ranges separated by ","

    Returns
    -------
    True if one range overlaps with the other, False otherwise

    Raises
    ------
    AttributeError: non-string arg provided
    IndexError: arg does not have ","
    """
    if fully_contains(assn_pair):
        return True
    secs1, secs2 = get_secs(assn_pair)
    test_secs = []
    if secs1 == get_extreme_secs(secs1, secs2, "lesser"):
        test_secs = secs1.split("-")
        other_secs = secs2.split("-")
    else:
        test_secs = secs2.split("-")
        other_secs = secs1.split("-")
    return int(test_secs[-1]) >= int(other_secs[0])


# Open input file and count relevant pairs for both challenge parts
num_containing_pairs = 0
num_overlap_pairs = 0
with open("./day4/day4_input.txt") as pairs_list:
    assn_pair = pairs_list.readline().strip()
    while assn_pair != "":
        if fully_contains(assn_pair):
            num_containing_pairs += 1
        if overlaps(assn_pair):
            num_overlap_pairs += 1
        assn_pair = pairs_list.readline().strip()

# Output total pairs with fully contained ranges and overlaps
print(num_containing_pairs, end=" ")
print("pairs have one range that fully contains the other")
print(num_overlap_pairs, end=" ")
print("pairs have ranges that overlap")
