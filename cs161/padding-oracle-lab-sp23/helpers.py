from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def pkcs7_pad(msg):
    padder = padding.PKCS7(128).padder()
    return padder.update(msg) + padder.finalize()

def pkcs7_unpad(padded_msg):
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded_msg) + unpadder.finalize()

def valid_pad(plaintext):
    try:
        pkcs7_unpad(plaintext)
        return True
    except ValueError:
        return False

def cbc_enc(key, iv, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext) + encryptor.finalize()

def cbc_dec(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def E(key, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    return cipher.decryptor().update(bytes(plaintext))

def D(key, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    return cipher.decryptor().update(bytes(ciphertext))

def xor_block(block1, block2):
    return bytes(a ^ b for a, b in zip(block1, block2))
