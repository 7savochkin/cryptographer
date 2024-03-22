from base.constants import ALPHABET


class SimpleAlphabetAdapter:
    """Simple Alphabet Adapter"""

    def __init__(self):
        self._alphabet = ALPHABET

    @property
    def alphabet(self):
        """
        Property for protected alphabet attr
        Realize only getter for this one
        """
        return self._alphabet

    @property
    def alphabet_length(self):
        return len(self.alphabet)

    def get_alphabet_char(self, index):
        return self.alphabet[index]
