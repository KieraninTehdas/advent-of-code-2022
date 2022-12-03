import sys
from collections import defaultdict


def find_max_calories(input_filename):

    elf_rations = defaultdict(int)
    elf_id = 0

    with open(input_filename, "r") as f:
        for calorie_count in f:
            if calorie_count == "\n":
                elf_id += 1
                continue
            else:
                elf_rations[elf_id] += int(calorie_count)

    return max(elf_rations.values())


if __name__ == "__main__":
    print(find_max_calories(sys.argv[1]))
