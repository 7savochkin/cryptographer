from abc import ABC, abstractmethod
from typing import Union, List

from base.adapters import SimpleAlphabetAdapter
from helpers import compare_chars_case


class BaseCryptographer(ABC):
    """Abstract class for cryptographers"""

    @abstractmethod
    def validate_key(self):
        """Validating key for encrypting/decrypting"""
        pass

    @abstractmethod
    def encrypt(self, data: str):
        """Encrypt data"""
        pass

    @abstractmethod
    def decrypt(self, data: str):
        """Decrypt data"""
        pass


class BaseSubstitutionCryptographer(BaseCryptographer, SimpleAlphabetAdapter):
    """Base class for substitution cryptographers"""

    def __init__(self, key: Union[int, List[int]]):
        super(BaseSubstitutionCryptographer, self).__init__()
        self.key = key

    @abstractmethod
    def get_encrypted_char(self, alphabet_index: int) -> str:
        """
        Get encrypted char from ALPHABET
        :param alphabet_index - index of char in ALPHABET
        :return encrypted_char
        """
        pass

    @abstractmethod
    def get_decrypted_char(self, alphabet_index):
        """
        Get decrypted char from ALPHABET
        :param alphabet_index - index of char in ALPHABET
        :return decrypted_char
        """
        pass

    def validate_key(self):
        if not self.key:
            raise KeyError('Key error is invalid')

    def encrypt(self, data: str):
        """
        Encrypt data by substitution algorithm
        :param data: data for encrypting
        :return: encrypted data
        """
        self.validate_key()
        encrypted_text = ''

        for char in data:
            # find index of char in alphabet
            alphabet_index = self.alphabet.find(char.upper())
            if char.isalpha():
                encrypted_char = self.get_encrypted_char(alphabet_index)
                encrypted_text += compare_chars_case(char, encrypted_char)
            else:
                encrypted_text += char

        return encrypted_text

    def decrypt(self, data: str):
        """
        Decrypt data by substitution algorithm
        :param data: data for decrypting
        :return: decrypted data
        """
        self.validate_key()
        decrypted_text = ''

        for char in data:
            # find index of char in alphabet
            alphabet_index = self.alphabet.find(char.upper())
            if char.isalpha():
                encrypted_char = self.get_decrypted_char(alphabet_index)
                decrypted_text += compare_chars_case(char, encrypted_char)
            else:
                decrypted_text += char

        return decrypted_text
