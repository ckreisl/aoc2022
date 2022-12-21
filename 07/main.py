from __future__ import annotations

from pathlib import Path
import sys


class File:

    def __init__(self, parent: Directory, name: str, size: int) -> None:
        self.parent = parent
        self.name = name
        self.size = size


class Directory:

    def __init__(self, parent, name) -> None:
        self.name = name 
        self.parent = parent
        self.__folders: list[Directory] = []
        self.__files: list[File] = []

    @property
    def folders(self) -> list[Directory]:
        return self.__folders

    @property
    def files(self) -> list[File]:
        return self.__files

    def is_root(self) -> bool:
        return self.parent == None

    def up(self) -> Directory:
        if self.is_root():
            return self
        return self.parent        

    def cd(self, name: str) -> Directory:
        for folder in self.__folders:
            if folder.name == name:
                return folder
        raise FileNotFoundError(f"Folder: {name} not found!")

    def add_folder(self, name: str) -> None:
        self.folders.append(
            Directory(name=name, parent=self))

    def add_file(self, name: str, size: int) -> None:
        self.files.append(
            File(parent=self, name=name, size=size))


class Tree:
    
    def __init__(self) -> None:
        self.root = Directory(None, "root")

    def parse(self, commands: list[str]) -> Tree:

        root = self.root

        for command in commands:
            if command == "$ ls":
                continue

            if command == "$ cd /":
                root = self.root
                continue

            if command == "$ cd ..":
                root = root.up()            
                continue

            if "$ cd" in command:
                _, target = command[2:].split()
                root = root.cd(target)
                continue        
            
            # Folder(s)
            if command.startswith("dir"):
                _, name = command.split()
                root.add_folder(name)
                continue
            
            # File(s)
            size, name = command.split()
            root.add_file(name, int(size))

        return self


def get_size(node: Directory) -> int:

    size = 0

    for file in node.files:
        size += file.size

    for folder in node.folders:
        size += get_size(folder)

    return size


def compute(node: Directory, MAX: int = 100000) -> int:

    result = 0

    size = get_size(node)
    if size <= MAX:
        # print(f"{size=}")
        result += size

    for folder in node.folders:
        result += compute(folder)

    return result


def solve_part1(content: str) -> None:
    # Ignore first "cd /"
    t = Tree().parse(content.splitlines()[1::])

    size = get_size(t.root)
    print(f"Size is: {size}")

    res = compute(t.root)
    print(f"Result is: {res}")


def find_smallest(node: Directory, required_space: int, smallest: list) -> list:
    
    size = get_size(node)
    if size >= required_space:
        smallest.append(size)

    for folder in node.folders:
        find_smallest(folder, required_space, smallest)

    return min(smallest)


def solve_part2(content: str) -> None:
    # Ignore first "cd /"
    t = Tree().parse(content.splitlines()[1::])

    size = get_size(t.root)
    free_space = 70000000 - size
    required_space = 30000000 - free_space

    xs = []
    print(f"Required space: {required_space}")
    print(f"Smallest: {find_smallest(t.root, required_space, xs)}")


def main() -> int:

    with open(Path(__file__).parent / "input.txt", encoding='utf-8') as f:
        content = f.read()

    solve_part1(content)
    solve_part2(content)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
