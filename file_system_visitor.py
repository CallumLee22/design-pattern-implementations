"""File system implemented using visitor pattern"""

from abc import ABC, abstractmethod


# Visitor interface
class Visitor(ABC):
    @abstractmethod
    def visit_file(self, file):
        pass

    @abstractmethod
    def visit_directory(self, directory):
        pass


# Component interface
class FileSystemComponent(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


# Concrete components
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def accept(self, visitor: Visitor):
        visitor.visit_file(self)


class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def accept(self, visitor: Visitor):
        visitor.visit_directory(self)
        for child in self.children:
            child.accept(visitor)


# Concrete visitors
class SizeVisitor(Visitor):
    def __init__(self):
        self.total = 0

    def visit_file(self, file):
        self.total += file.size

    def visit_directory(self, directory):
        pass


class DisplayVisitor(Visitor):
    def __init__(self):
        self.indent = 0

    def visit_file(self, file):
        print(" " * self.indent + f"File: {file.name} ({file.size} KB)")

    def visit_directory(self, directory):
        print(" " * self.indent + f"Directory: {directory.name}")
        self.indent += 2


root = Directory("root")
sub = Directory("subdir")
root.add(sub)
sub.add(File("a.txt", 10))
root.add(File("b.txt", 20))
print("File system:")
display = DisplayVisitor()
root.accept(display)
size = SizeVisitor()
root.accept(size)
print(f"Total size: {size.total} KB")
