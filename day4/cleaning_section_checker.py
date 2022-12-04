import sys


def _ranges_overlap(range1, range2):
    return (range1[0] <= range2[0] and range1[1] >= range2[1]) or (
        range2[0] <= range1[0] and range2[1] >= range1[1]
    )


def find_dupicated_assignments(assignments_filename):
    counter = 0

    with open(assignments_filename, "r") as f:
        for assignment_pair in f:
            assignments = [
                [int(r) for r in a.split("-")]
                for a in assignment_pair.strip().split(",")
            ]

            if _ranges_overlap(assignments[0], assignments[1]):
                counter += 1

    return counter


if __name__ == "__main__":
    print(find_dupicated_assignments(sys.argv[1]))
