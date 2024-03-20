from base.cryptographer import BaseSubstitutionCryptographer


class CaezarCryptographer(BaseSubstitutionCryptographer):
    """Caezar's Cryptographer"""

    def validate_key(self) -> None:
        """Validate key of encrypting/decrypting"""
        super(CaezarCryptographer, self).validate_key()
        if self.key < 0 or self.key > 33:
            raise KeyError(
                'Key must be less than 34 symbols and bigger than -1')

    def get_encrypted_char(self, alphabet_index: int) -> str:
        encrypted_index = alphabet_index + self.key
        return self.get_alphabet_char(encrypted_index)

    def get_decrypted_char(self, alphabet_index: int) -> str:
        decrypted_index = alphabet_index - self.key
        return self.get_alphabet_char(decrypted_index)
