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
        self.children = []

        if directory:
            self.directory.add_file(self)

    def file_type(self):
        return FileType.DIRECTORY

    def calculate_size(self):
        return sum([child.calculate_size() for child in self.children])

    def add_file(self, file):
        self.children.append(file)

    def list(self):
        return self.children

    def __str__(self):
        return str({self.name: [str(child) for child in self.children]})

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

    # Unused for now
    def execute_command(self, command_string):
        commands = {"ls": self.list, "cd": self.change_directory}
        split_command = command_string.split(" ")

        command = split_command[0]

        if len(split_command) == 1:
            argument = ""
        else:
            argument = split_command[1]

        return commands[command](argument)

    def go_to_root_directory(self):
        while self.current_directory.directory:
            self.change_directory("..")

    def list(self, file_type_filter: Optional[FileType] = None):
        if file_type_filter:
            return filter(
                lambda f: f.file_type() == file_type_filter,
                self.current_directory.children,
            )
        else:
            return self.current_directory.children

    def change_directory(self, target):
        if target == "..":
            if self.current_directory.directory is None:
                return
            self.current_directory = self.current_directory.directory
        elif target == self.current_directory.name:
            return
        else:
            target_directory = next(
                filter(
                    lambda f: f.file_type() == FileType.DIRECTORY and f.name == target,
                    self.current_directory.children,
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
                        fs.current_directory.children,
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
                        fs.current_directory.children,
                    ),
                    None,
                )

                if not existing_file:
                    File(file_name, int(tokens[0]), fs.current_directory)

    fs.go_to_root_directory()
    return fs


if __name__ == "__main__":

    fs = parse_filesystem(sys.argv[1])
    print(fs.current_directory.name)
    pprint(fs.execute_command("ls"))
