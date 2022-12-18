# CHALLENGE INTRO:
# Each line of the file day3_input.txt represents the items contained
# inside a rucksack. A rucksack has two compartments. Each compartment
# contains one of two halves of the items in the rucksack. Items are
# represented by alphabetic characters. Each character corresponds to
# a numerical priority:
#       Lowercase characters 'a' through 'z': Priorities 1 through 26
#       Uppercase characters 'A' through 'Z': Priorities 27 through 52
#
# PART 1:
# For each rucksack, there exists exactly 1 item that is present in
# both compartments. Determine the sum of the priorities for these
# items in all rucksacks.
#
# PART 2:
# Each rucksack is carried by an elf. Elves are divided into groups of
# 3. There exists exactly 1 item that is present in all three rucksacks
# in a group of elves. Determine the sum of the priorities for these
# items in all elf groups.


def create_rucksack(items):
    """
    Return representation of rucksack as tuple given string of items.

    Args
    ----
    items: string representing a rucksack's items

    Returns
    -------
    tuple with two strings representing rucksack compartments
       
    Raises
    ------
    TypeError: provided items param is not iterable
    """
    halfway_pt = len(items) // 2
    return (items[:halfway_pt], items[halfway_pt:])


def find_common_item(*groups):
    """
    Returns an item present in all provided arguments.

    Args
    ----
    *groups: iterables to find common items in

    Returns
    -------
    1 item present in all args; if more than 1 exists, returns
    randomly selected common item
       
    Raises
    ------
    TypeError: at least one provided groups arg is not iterable
    KeyError: no common items exist between args
    """
    common_items = set(groups[0])
    for i in range(1, len(groups)):
        next_set = set(groups[i])
        common_items = common_items.intersection(next_set)
    return common_items.pop()


def get_priority(char):
    """
    Returns numerical priority corresponding to provided char.

    Args
    ----
    char: one-character string to convert

    Returns
    -------
    int representing the priority of char
       
    Raises
    ------
    AttributeError: arg is not type string
    TypeError: arg is string, but of length other than 1
    """
    if char.islower():
        return ord(char) - 96
    return ord(char) - (65-27)


def sum_priorities(chars):
    """
    Returns sum of priorities corresponding to list of chars.

    Args
    ----
    chars: iterable containing one-character strings

    Returns
    -------
    int sum of priorities associated with each char
       
    Raises
    ------
    TypeError: provided chars param is not iterable
    """
    ret = []
    for char in chars:
        ret.append(get_priority(char))
    return sum(ret)


# Open input file and build lists of common items
input_stream = open("./day3/day3_input.txt")
sack_commons = []
elf_group = []
group_commons = []
for rucksack in input_stream:
    rucksack = rucksack.strip()
    # Find common items in each rucksack compartment
    compart1, compart2 = create_rucksack(rucksack)
    sack_commons.append(find_common_item(compart1, compart2))
    # Find common items in three-elf groups
    elf_group.append(rucksack)
    if len(elf_group) == 3:
        elf1, elf2, elf3 = elf_group
        group_commons.append(find_common_item(elf1, elf2, elf3))
        elf_group = []

# Output sums of priorities
common_sum = sum_priorities(sack_commons)
print(f"Part 1: The sum of the priorities is {common_sum}")
common_sum = sum_priorities(group_commons)
print(f"Part 2: The sum of the priorities is {common_sum}")

# Close input stream
input_stream.close()
