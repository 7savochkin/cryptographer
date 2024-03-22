from base import BaseSubstitutionCryptographer


class AffineCryptographer(BaseSubstitutionCryptographer):
    """Affine's Cryptographer"""

    def get_encrypted_char(self, alphabet_index: int) -> str:
        k, t = self.key

        encrypted_index = (alphabet_index * k + t) % self.alphabet_length
        return self.get_alphabet_char(encrypted_index)

    def get_decrypted_char(self, alphabet_index: int) -> str:
        k, t = self.key

        mod_k = pow(k, -1, len(self.alphabet))
        mod_t = (-mod_k * t) % len(self.alphabet)

        decrypted_index = (alphabet_index * mod_k + mod_t) % len(self.alphabet)
        return self.get_alphabet_char(decrypted_index)
