import sys
from pprint import pprint
from enum import Enum


class FileType(Enum):
    FILE = 1
    DIRECTORY = 2


class Directory:
    def __init__(self, name, directory=None, children=None):
        self.name = name
        self.directory = directory

        if directory:
            self.directory.add_file(self)

        if children is None:
            self.children = []
        else:
            self.children = children

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


def _construct_filesystem(terminal_output):
    pass


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

    def execute_command(self, command_string):
        commands = {"ls": self._list, "cd": self._change_directory}
        split_command = command_string.split(" ")

        command = split_command[0]

        if len(split_command) == 1:
            argument = ""
        else:
            argument = split_command[1]

        return commands[command](argument)

    def _list(self, _):
        return self.current_directory.list()

    def _change_directory(self, target):
        if target == "..":
            self.current_directory = self.current_directory.directory
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


if __name__ == "__main__":
    fs = Filesystem("/")
    file1 = File("file1", 256, fs.current_directory)
    file2 = File("file2", 20, fs.current_directory)
    dir1 = Directory("d", fs.current_directory)
    file3 = File("file3", 500, dir1)

    pprint(fs.execute_command("ls"))
