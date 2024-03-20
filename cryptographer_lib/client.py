from base.cryptographer import BaseCryptographer


class ClientCryptographer(BaseCryptographer):
    """Client for cryptographers"""

    def __init__(self, crypto_instance: BaseCryptographer):
        """
        :param crypto_instance: instance of cryptographer
        """
        self.crypto_instance = crypto_instance

    def validate_key(self):
        return self.crypto_instance.validate_key()

    def encrypt(self, data: str):
        return self.crypto_instance.encrypt(data)

    def decrypt(self, data: str):
        return self.crypto_instance.decrypt(data)
