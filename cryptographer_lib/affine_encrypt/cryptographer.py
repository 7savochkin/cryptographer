from base import BaseSubstitutionCryptographer


class AffineCryptographer(BaseSubstitutionCryptographer):
    """Affine's Cryptographer"""

    def get_encrypted_char(self, alphabet_index: int) -> str:
        encrypted_index = (alphabet_index * self.key[0] + self.key[1]) % len(self.alphabet)
        return self.get_alphabet_char(encrypted_index)

    def get_decrypted_char(self, alphabet_index: int) -> str:
        mod_inv = pow(self.key[0], -1, int(len(self.alphabet) / 2))
        decrypted_index = ((alphabet_index - self.key[1]) * mod_inv) % len(self.alphabet)
        return self.get_alphabet_char(decrypted_index)
