import sys
from pprint import pprint


class Directory:
    def __init__(self, name, directory=None, children=None):
        self.name = name
        self.directory = directory

        if directory:
            self.directory.add_child(self)

        if children is None:
            self.children = []
        else:
            self.children = children

    def calculate_size(self):
        return sum([child.calculate_size() for child in self.children])

    def add_child(self, file):
        self.children.append(file)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class File:
    def __init__(self, name, size, directory):
        self.name = name
        self.size = size
        self.directory = directory
        self.directory.add_child(self)

    def calculate_size(self):
        return self.size

    def __str__(self):
        return f"{self.name} ({self.size})"

    def __repr__(self):
        return f"{self.name} ({self.size})"


def _construct_filesystem(terminal_output):
    pass


if __name__ == "__main__":
    pass
