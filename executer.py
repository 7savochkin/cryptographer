from cryptographer_lib.affine_encrypt import AffineCryptographer
from cryptographer_lib.caezar_encrypt import CaezarCryptographer
from cryptographer_lib.linear_encrypt import LinearCryptographer
from cryptographer_lib import ClientCryptographer


def test_caezar_cryptographer():
    clean_text = 'Я, Савочкін Олег Олександрович, студент університету'
    key = 3

    client = ClientCryptographer(
        crypto_instance=CaezarCryptographer(key)
    )

    encrypted = client.encrypt(clean_text)

    print(f'Encrypted: {encrypted}')

    decrypted = client.decrypt(encrypted)

    print(f'Decrypted: {decrypted}')


def test_linear_cryptographer():
    clean_text = 'Я, Савочкін Олег Олександрович, студент університету'
    key = 2

    client = ClientCryptographer(
        crypto_instance=LinearCryptographer(key)
    )

    encrypted = client.encrypt(clean_text)

    print('Encrypted: ' + encrypted)

    decrypted = client.decrypt(encrypted)

    print('Decrypted: ' + decrypted)


def test_affine_cryptographer():
    clean_text = 'Я, Савочкін Олег Олександрович, студент університету'
    key = [2, 5]

    client = ClientCryptographer(
        crypto_instance=AffineCryptographer(key)
    )

    encrypted = client.encrypt(clean_text)

    print('Encrypted: ' + encrypted)

    decrypted = client.decrypt(encrypted)

    print('Decrypted: ' + decrypted)


print('Caezar: \n')
test_caezar_cryptographer()
print('---------------------------------')
print('Linear: \n')
test_linear_cryptographer()
print('---------------------------------')
print('Affine: \n')
test_affine_cryptographer()
print('---------------------------------')