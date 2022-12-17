# CHALLENGE INTRO:
# 

# For each rucksack, split elements in half and convert to sets
# intersect the sets and pop the element to get common item
# ord() to get encoding number, then subtract accordingly

def create_rucksack(items):
    halfway_pt = len(items) // 2
    return (items[:halfway_pt], items[halfway_pt:])


def find_common_item(rucksack):
    compart1, compart2 = rucksack
    compart1 = set(compart1)
    compart2 = set(compart2)
    common_item = compart1.intersection(compart2)
    return common_item.pop()


def get_priority(char):
    if char.islower():
        return ord(char) - 96
    return ord(char) - (65-27)


def get_priority_list(file):
    ret = []
    items = file.readline().strip()
    while items != "":
        rucksack = create_rucksack(items)
        priority = get_priority(find_common_item(rucksack))
        ret.append(priority)
        items = file.readline().strip()
    return ret


input_stream = open("./day3/day3_input.txt")
priority_list = get_priority_list(input_stream)
input_stream.close()
print(f"The sum of the priorities is {sum(priority_list)}")
