"""File system implementation using decorator pattern"""

from abc import ABC, abstractmethod


# Base component
class FileSystemComponent(ABC):
    """File system component interface"""

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def display(self):
        pass


class File(FileSystemComponent):
    """Concrete file component"""

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def display(self):
        print(f"File: {self.name} ({self.size} KB)")


class FileDecorator(FileSystemComponent):
    """Base decorator"""

    def __init__(self, wrapped: FileSystemComponent):
        self._wrapped = wrapped

    def get_size(self):
        return self._wrapped.get_size()

    def display(self):
        self._wrapped.display()


# Concrete decorators
class CompressedFile(FileDecorator):
    """Concrete decorator for compression"""

    def get_size(self):
        original = self._wrapped.get_size()
        return int(original * 0.5)

    def display(self):
        print("[Compressed]", end=" ")
        self._wrapped.display()


class EncryptedFile(FileDecorator):
    """Concrete decorator for encrypting"""

    def get_size(self):
        return self._wrapped.get_size() + 5  # overhead

    def display(self):
        print("[Encrypted]", end=" ")
        self._wrapped.display()


class LoggingFile(FileDecorator):
    """Concrete decorator for logging"""

    def get_size(self):
        size = self._wrapped.get_size()
        print(f"[LOG] Size requested: {size} KB")
        return size

    def display(self):
        print("[LOG] Displaying file:")
        self._wrapped.display()


file = File("data.txt", 100)

# Wrap with decorators
file = CompressedFile(file)
file = EncryptedFile(file)
file = LoggingFile(file)
file.display()
print(f"Final size: {file.get_size()} KB")
