import sys
from pprint import pprint
from enum import Enum
from typing import Optional


class FileType(Enum):
    FILE = 1
    DIRECTORY = 2


class Directory:
    def __init__(self, name, directory=None):
        self.name = name
        self.directory = directory
        self.files = []

        if directory:
            self.directory.add_file(self)

    def file_type(self):
        return FileType.DIRECTORY

    def calculate_size(self):
        return sum([child.calculate_size() for child in self.files])

    def add_file(self, file):
        self.files.append(file)

    def list(self):
        return self.files

    def list_dirs(self):
        return filter(
            lambda f: f.file_type() == FileType.DIRECTORY,
            self.files,
        )

    def __str__(self):
        return str({self.name: [str(child) for child in self.files]})

    def __repr__(self):
        return str(self)


class File:
    def __init__(self, name, size, directory):
        self.name = name
        self.size = size
        self.directory = directory
        self.directory.add_file(self)

    def file_type(self):
        return FileType.FILE

    def calculate_size(self):
        return self.size

    def __str__(self):
        return f"{self.name} ({self.size})"

    def __repr__(self):
        return str(self)


class DirectoryUnknownError(Exception):
    def __init__(self, current_directory, target_directory):
        self.target_directory = target_directory
        self.current_directory = current_directory
        super().__init__(
            f"Can't move to {target_directory} from {current_directory} - directory unknown"
        )


class Filesystem:
    def __init__(self, root_directory_name):
        self.root_directory = Directory(root_directory_name)
        self.current_directory: Directory = self.root_directory

    def go_to_root_directory(self):
        while self.current_directory.directory:
            self.change_directory("..")

    def change_directory(self, target):
        if target == "..":
            if self.current_directory.directory is None:
                return
            self.current_directory = self.current_directory.directory
        else:
            target_directory = next(
                filter(
                    lambda f: f.file_type() == FileType.DIRECTORY and f.name == target,
                    self.current_directory.files,
                ),
                None,
            )

            if target_directory is None:
                raise DirectoryUnknownError(self.current_directory, target_directory)

            self.current_directory = target_directory


def parse_filesystem(filename):
    fs = Filesystem("/")

    with open(filename, "r") as f:
        for line in f:
            tokens = line.strip().split(" ")
            if tokens[0] == "$":
                if tokens[1] == "cd":
                    fs.change_directory(tokens[2])
                else:
                    continue
            elif tokens[0] == "dir":
                dir_name = tokens[1]
                existing_dir = next(
                    filter(
                        lambda f: f.file_type() == FileType.DIRECTORY
                        and f.name == dir_name,
                        fs.current_directory.files,
                    ),
                    None,
                )

                if not existing_dir:
                    Directory(dir_name, fs.current_directory)
            else:
                file_name = tokens[1]

                existing_file = next(
                    filter(
                        lambda f: f.file_type() == FileType.FILE
                        and f.name == file_name,
                        fs.current_directory.files,
                    ),
                    None,
                )

                if not existing_file:
                    File(file_name, int(tokens[0]), fs.current_directory)

    fs.go_to_root_directory()
    return fs


def calculate_total_branch_size(_dir, previous_total=0, size_limit=100000):
    dir_size = _dir.calculate_size()

    next_total = previous_total
    if dir_size < size_limit:
        next_total += dir_size

    for sub_dir in _dir.list_dirs():
        next_total = calculate_total_branch_size(sub_dir, next_total)

    return next_total


def part_one():
    size_limit = 100000

    fs = parse_filesystem(sys.argv[1])

    total_size = 0

    if fs.current_directory.calculate_size() < size_limit:
        total_size += fs.current_directory.calculate_size()

    for _dir in fs.current_directory.list_dirs():
        total_size += calculate_total_branch_size(_dir)

    print(total_size)


def calculate_min_branch_size(_dir, min_size, previous_min=None):
    dir_size = _dir.calculate_size()

    if dir_size > min_size:
        if previous_min is None:
            previous_min = dir_size
        elif dir_size < previous_min:
            previous_min = dir_size

    for sub_dir in _dir.list_dirs():
        previous_min = calculate_min_branch_size(sub_dir, min_size, previous_min)

    return previous_min


def part_two():
    total_space = 70000000
    target_free_space = 30000000

    fs = parse_filesystem(sys.argv[1])

    current_free_space = total_space - fs.root_directory.calculate_size()

    min_target_dir_size = target_free_space - current_free_space

    min_dir_size = None

    root_size = fs.current_directory.calculate_size()
    if root_size > min_target_dir_size:
        min_dir_size = root_size

    for _dir in fs.current_directory.list_dirs():
        min_dir_size = calculate_min_branch_size(
            _dir, min_target_dir_size, min_dir_size
        )

    print(min_dir_size)


if __name__ == "__main__":
    part_two()
