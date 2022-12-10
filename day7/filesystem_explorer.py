import sys
from pprint import pprint
from enum import Enum


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
        print(f"Executing command `{command_string}`")

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


if __name__ == "__main__":
    fs = Filesystem("/")

    with open(sys.argv[1], "r") as f:
        for line in f:
            print(fs.current_directory)
            tokens = line.strip().split(" ")
            if tokens[0] == "$":
                if tokens[1] == "cd":
                    fs.execute_command(" ".join(tokens[1:]))
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
                    print(f"Adding dir {dir_name} to {fs.current_directory.name}")
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
                    print(f"Adding file {file_name} to {fs.current_directory.name}")
                    File(file_name, int(tokens[0]), fs.current_directory)

    fs.execute_command("cd ..")
    fs.execute_command("cd ..")
    fs.execute_command("cd ..")
    fs.execute_command("cd ..")
    pprint(fs.current_directory.name)
    pprint(fs.execute_command("ls"))
