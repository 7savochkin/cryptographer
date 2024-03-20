from base.cryptographer import BaseSubstitutionCryptographer


class LinearCryptographer(BaseSubstitutionCryptographer):
    """Linear's Cryptographer"""

    def get_encrypted_char(self, alphabet_index: int) -> str:
        encrypted_index = int(alphabet_index * self.key % (len(self.alphabet) / 2))
        return self.get_alphabet_char(encrypted_index)

    def get_decrypted_char(self, alphabet_index: int) -> str:
        mod_inv = pow(self.key, -1, int(len(self.alphabet)/2))
        decrypted_index = int(alphabet_index * mod_inv % (len(self.alphabet) / 2))
        return self.get_alphabet_char(decrypted_index)
