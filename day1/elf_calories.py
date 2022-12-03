import sys
from collections import defaultdict


class ElfRations:
    def __init__(self, input_filename):
        self.elf_rations = defaultdict(int)
        elf_id = 0

        with open(input_filename, "r") as f:
            for calorie_count in f:
                if calorie_count == "\n":
                    elf_id += 1
                    continue
                else:
                    self.elf_rations[elf_id] += int(calorie_count)

    def max_calories(self):
        return max(self.elf_rations.values())

    def top_n_elves_total_calories(self, n=3):
        return sum(sorted(self.elf_rations.values(), reverse=True)[:3])


if __name__ == "__main__":
    elf_rations = ElfRations(sys.argv[1])
    print(elf_rations.top_n_elves_total_calories())
