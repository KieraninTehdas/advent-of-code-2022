import sys
from typing import Tuple


def _calculate_priority(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


def _get_compartments(rucksack_contents: str) -> Tuple[str, str]:
    first_compartment_contents = rucksack_contents[: int(len(rucksack_contents) / 2)]
    second_compartment_contents = rucksack_contents[int(len(rucksack_contents) / 2) :]

    return (first_compartment_contents, second_compartment_contents)


def _find_common_items(rucksack_contents):
    first_compartment_contents = _get_compartments(rucksack_contents)[0]
    second_compartment_contents = _get_compartments(rucksack_contents)[1]
    return list(
        set(first_compartment_contents).intersection(second_compartment_contents)
    )


def common_item_priority_total(input_filename):
    total = 0

    with open(input_filename, "r") as f:
        for rucksack_contents in f:
            common_items = _find_common_items(rucksack_contents)

            total += sum(map(_calculate_priority, common_items))

    return total


if __name__ == "__main__":
    print(common_item_priority_total(sys.argv[1]))
