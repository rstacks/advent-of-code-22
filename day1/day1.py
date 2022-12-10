# CHALLENGE INTRO:
# Santa's elves are carrying food items for a journey into the jungle.
# Each food item has a certain number of calories. The file
# day1_input.txt contains the calorie count of each food item on a
# separate line. Each elves' food collection is separated by a blank
# line.
#
# PART 1:
# Determine the total number of calories carried by the elf with the
# most calories.
#
# PART 2:
# Determine the total number of calories carried by the top three elves
# carrying the most calories.


def store_elf_data(current_elf_data, all_elf_data):
    """
    Store current elf's calorie sum in provided list.

    Args
    ----
    current_elf_data: int list of current elf's calorie counts
    all_elf_data: int list containing all elves' calorie sums
    
    Returns
    -------
    None
    
    Raises
    ------
    TypeError: provided param(s) contain non-numeric elements
    """
    all_elf_data.append(sum(current_elf_data))


def is_cal_count(str):
    """
    Returns True if param contains a calorie count.

    Args
    ----
    str: string to be evaluated
    
    Returns
    -------
    True if str contains a calorie count, False otherwise
    
    Raises
    ------
    TypeError: provided param is not string
    """
    if len(str) <= 1:
        return False
    return True


def top_count(all_elf_data, num):
    """
    Sum calories for top num calorie-carrying elves.

    Args
    ----
    all_elf_data: int list of all elves' calorie sums
    num: int number of highest calorie carriers to sum
    
    Returns
    -------
    int sum of calorie counts from top num calorie carriers
    
    Raises
    ------
    TypeError: provided list param contains non-numeric elements
    TypeError: provided num param is not int
    ValueError: list param has too few elements given num param
    """
    copied_data = all_elf_data[:]
    sum = 0
    for i in range(num):
        sum += max(copied_data)
        copied_data.remove(max(copied_data))
    return sum


# Open input file and prepare lists for storing calorie counts
cal_file = open("./day1/day1_input.txt")
current_line = cal_file.readline()
elf_data = []
all_data = []

# Iterate over cal_file to grab all calorie counts
# Note calorie counts for current elf, then reset elf_data for next elf
while current_line != "":
    if is_cal_count(current_line):
        elf_data.append(int(current_line.strip()))
    else:
        store_elf_data(elf_data, all_data)
        elf_data = []
    current_line = cal_file.readline()

# Close cal_file
cal_file.close()

# PART 1 Output
print(f"The elf with the most calories has {max(all_data)} calories")

# PART 2 Output
print("The calories carried by the top 3 elves is", end=" ")
print(f"{top_count(all_data, 3)} calories")
