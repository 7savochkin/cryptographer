from abc import ABC, abstractmethod


class BaseFileEditor(ABC):
    """Abstract class for file editors"""

    def __init__(self, encoding: str = 'utf-8'):
        self.encoding = encoding

    @abstractmethod
    def read_file(self, path: str):
        """Read file by path"""
        pass

    @abstractmethod
    def write_file(self, path: str, body: str):
        """Create or write body to file by path"""
        pass


class DefaultFileEditor(BaseFileEditor):
    """Default editor for file"""

    def read_file(self, path: str) -> str:
        """
        Read file by path
        :param path - path to file
        :return data of file
        """
        with open(path, 'r', encoding=self.encoding) as file:
            return file.read()

    def write_file(self, path: str, body: str) -> str:
        """
        Create or write body to file
        :param path - path to file
        :param body - data to write
        :return path of file
        """
        with open(path, 'w', encoding=self.encoding) as file:
            file.write(body)
        return path
