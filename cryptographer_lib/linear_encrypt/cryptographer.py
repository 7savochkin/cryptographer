from base.cryptographer import BaseSubstitutionCryptographer


class LinearCryptographer(BaseSubstitutionCryptographer):
    """Linear's Cryptographer"""

    def get_encrypted_char(self, alphabet_index: int) -> str:
        encrypted_index = (alphabet_index * self.key) % self.alphabet_length

        return self.get_alphabet_char(encrypted_index)

    def get_decrypted_char(self, alphabet_index: int) -> str:
        mod_k = pow(self.key, -1, self.alphabet_length)

        decrypted_index = (alphabet_index * mod_k) % self.alphabet_length
        return self.get_alphabet_char(decrypted_index)
