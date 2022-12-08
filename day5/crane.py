import sys
from collections import deque, defaultdict, namedtuple
from pprint import pprint

Instruction = namedtuple("Instruction", "n_to_move source_stack target_stack")


def _initialise_stacks(input_filename):
    stacks = defaultdict(deque)

    with open(input_filename, "r") as f:
        end_of_stacks_reached = False

        for line in f:
            if end_of_stacks_reached:
                break

            for stack_number, column_number in enumerate(range(1, len(line) + 1, 4)):

                char = line[column_number]

                if char.isnumeric():
                    end_of_stacks_reached = True
                    break

                if line[column_number] != " ":
                    stacks[stack_number + 1].appendleft(line[column_number])

        return [item[1] for item in sorted(stacks.items(), key=lambda i: int(i[0]))]


def _instructions(input_filename):
    with open(input_filename, "r") as f:
        for line in f:
            commands = line.strip("\n").split(" ")

            if commands[0] != "move":
                continue

            yield Instruction(
                int(commands[1]), int(commands[3]) - 1, int(commands[5]) - 1
            )


if __name__ == "__main__":
    stacks = _initialise_stacks(sys.argv[1])
    for instruction in _instructions(sys.argv[1]):
        crates_to_move = deque()
        for _ in range(0, instruction.n_to_move):
            crates_to_move.appendleft(stacks[instruction.source_stack].pop())

        stacks[instruction.target_stack].extend(crates_to_move)

    top_crates = "".join([stack[-1] for stack in stacks])

    print(top_crates)
