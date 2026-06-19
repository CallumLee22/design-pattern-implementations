"""
This file system implementation uses the composite pattern
"""

from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    """Interface for a component of the file system"""

    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the component"""

    @abstractmethod
    def display(self, indent=0):
        """Show the component"""


class File(FileSystemComponent):
    """File in the file system"""

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def display(self, indent=0):
        print(" " * indent + f"File: {self.name} ({self.size} KB)")


class Directory(FileSystemComponent):
    """Representing a directory in a file system"""

    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        """Add a file system component as a child"""
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        """Remove a file system component as a child"""
        self.children.remove(component)

    def get_size(self):
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

    def display(self, indent=0):
        print(" " * indent + f"Directory: {self.name}")
        for child in self.children:
            child.display(indent + 2)


if __name__ == "__main__":
    # Create files
    file1 = File("file1.txt", 10)
    file2 = File("file2.txt", 10)
    file3 = File("file3.txt", 50)

    # Create directories
    root = Directory("root")
    sub_dir1 = Directory("subdir1")
    sub_dir2 = Directory("subdir2")

    # Build file system structure
    sub_dir1.add(file1)
    sub_dir1.add(file2)

    sub_dir2.add(file3)

    root.add(sub_dir1)
    root.add(sub_dir2)

    # Display hierarchy
    root.display()

    print(f"Total size of file system is {root.get_size()} KB")
