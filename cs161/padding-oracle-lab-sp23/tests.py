from os import devnull
import secrets
import sys
import textwrap

from helpers import cbc_enc, D, pkcs7_pad, pkcs7_unpad, valid_pad, xor_block

# Some of these autograder test a function that might sometimes return the
# correct value and sometimes return the incorrect value. This variable controls
# how many times these tests will be run to mitigate this.
_AUTOGRADER_ROUNDS = 64

def test1(invalid_last_byte):
    EXPLANATION_MSG = textwrap.dedent("""\
    Anything but 1 and 5 that is between [0,256] works.
    This is because 1 as the last byte always produces a valid padding (consider why!) and 5 is the padding we would've expected in a valid padding of a 43-byte message (distance from 43 to the next multiple of 16 is 5).
    """).strip()

    msg = b"THIS IS A TEST! Let's see if padding works!"
    padded_msg = pkcs7_pad(msg)

    if not (type(invalid_last_byte) == int):
        print('`invalid_last_byte` must be a number')
        return False

    invalid_msg = bytearray(padded_msg)
    invalid_msg[-1] = invalid_last_byte

    if valid_pad(bytes(invalid_msg)):
        print('`invalid_msg` should have invalid padding')
        return False

    print(f'All tests passed!\n\n{EXPLANATION_MSG}')
    return True

def test2(valid_last_byte_1, valid_last_byte_2):
    EXPLANATION_MSG = textwrap.dedent("""\
    1 always works in this case and 2 works because distance from 78 to the next multiple of 16 is 2.
    """).strip()

    msg = b"As part of a new test, let's try to run a different input and see if it works!"
    padded_msg = pkcs7_pad(msg)

    if not (type(valid_last_byte_1) == int and type(valid_last_byte_2) == int):
        print('Your valid bytes must be integers!')
        return False

    valid_msg_1 = bytearray(padded_msg)
    valid_msg_1[-1] = valid_last_byte_1

    valid_msg_2 = bytearray(padded_msg)
    valid_msg_2[-1] = valid_last_byte_2

    if not (1 <= valid_last_byte_1 <= 16 and 1 <= valid_last_byte_2 <= 16):
        print('Your valid bytes must be in the range [1, 16]')
        return False

    if valid_last_byte_1 == valid_last_byte_2:
        print('Your valid bytes must be different from each other.')
        return False

    if not valid_pad(bytes(valid_msg_1)):
        print('`valid_last_byte_1` did not result in valid padding!')
        return False
    if not valid_pad(bytes(valid_msg_2)):
        print('`valid_last_byte_2` did not result in valid padding!')
        return False

    print(f'All tests passed!\n\n{EXPLANATION_MSG}')
    return True

def test3(recover_last_byte):
    EXPLANATION_MSG = textwrap.dedent("""\
    There are only 256 options for a byte, so we go through all 256 options and identify the value of x that produces a valid padding that is not the original byte (i.e. x != 0).
    This must be the value of x that, when XORed with the plaintext, produces the plaintext byte 0x01.
    """).strip()

    num_correct = 0
    for i in range(_AUTOGRADER_ROUNDS):
        key = secrets.token_bytes(16)
        iv = secrets.token_bytes(16)
        plaintext = secrets.token_bytes(16 + secrets.randbelow(16))
        plaintext_padded = pkcs7_pad(plaintext)
        ciphertext = cbc_enc(key, iv, plaintext_padded)
        c1 = ciphertext[:16]
        c2 = ciphertext[16:]

        def oracle(C_prev, C):
            return valid_pad(xor_block(C_prev, D(key, C)))

        if recover_last_byte(oracle, bytearray(c1), bytearray(c2)) == plaintext_padded[31]:
            num_correct += 1

    if num_correct == _AUTOGRADER_ROUNDS:
        print(f'All tests passed!\n\n{EXPLANATION_MSG}')
        return True
    else:
        print(f'The recovered last byte is incorrect (correct {num_correct} / {_AUTOGRADER_ROUNDS} times)')
        return False

def test4(recover_second_last_byte):
    EXPLANATION_MSG = textwrap.dedent("""\
    Use recover_last_byte to find the last byte of the plaintext P_n[16].
    Then, XOR the last byte of the ciphertext with P_n[16] ^ 0x02 so the last plaintext byte will be 0x02.
    Then, repeat the technique used to bruteforce the second-to-last byte.
    """).strip()

    num_correct = 0
    for i in range(_AUTOGRADER_ROUNDS):
        key = secrets.token_bytes(16)
        iv = secrets.token_bytes(16)
        plaintext = secrets.token_bytes(16 + secrets.randbelow(16))
        plaintext_padded = pkcs7_pad(plaintext)
        ciphertext = cbc_enc(key, iv, plaintext_padded)
        c1 = ciphertext[:16]
        c2 = ciphertext[16:]

        def oracle(C_prev, C):
            return valid_pad(xor_block(C_prev, D(key, C)))

        if recover_second_last_byte(oracle, bytearray(c1), bytearray(c2)) == plaintext_padded[30]:
            num_correct += 1

    if num_correct == _AUTOGRADER_ROUNDS:
        print(f'All tests passed!\n\n{EXPLANATION_MSG}')
        return True
    else:
        print(f'The recovered last byte is incorrect (correct {num_correct} / {_AUTOGRADER_ROUNDS} times)')
        return False

def test5(decryption_fn):
    EXPLANATION_MSG = textwrap.dedent("""\
    The big idea behind the padding oracle attack is to recurse on the pattern that we began in the prior parts of Q2.
    We can reconstruct the last byte as shown in 2.2 and 2.3.
    We can use a similar process to get a valid two-byte padding and the second-to-last byte.
    Then, from there, we can repeat this search until we get the last byte.

    See https://research.nccgroup.com/2021/02/17/cryptopals-exploiting-cbc-padding-oracles/ for more detail!
    """).strip()

    key = secrets.token_bytes(16)
    iv = secrets.token_bytes(16)
    plaintext = secrets.token_bytes(16 * 2 + 12)
    plaintext_padded = pkcs7_pad(plaintext)
    ciphertext = cbc_enc(key, iv, plaintext_padded)
    c1 = ciphertext[:16]
    c2 = ciphertext[16:32]
    c3 = ciphertext[32:]

    def oracle(C_prev, C):
        return valid_pad(xor_block(C_prev, D(key, C)))

    if not bytes(decryption_fn(oracle, bytearray(c2), bytearray(c3))) == plaintext_padded[32:]:
        print('Third block did not decrypt correctly.')
        print(f'You gave me {bytes(decryption_fn(oracle, bytearray(c2), bytearray(c3)))}, but I expected {plaintext_padded[32:]}')
        return False
    if not bytes(decryption_fn(oracle, bytearray(c1), bytearray(c2))) == plaintext_padded[16:32]:
        print('Second block did not decrypt correctly.')
        print(f'You gave me {bytes(decryption_fn(oracle, bytearray(c2), bytearray(c3)))}, but I expected {plaintext_padded[16:32]}')
        return False
    if not bytes(decryption_fn(oracle, bytearray(iv), bytearray(c1))) == plaintext_padded[:16]:
        print('First block did not decrypt correctly.')
        print(f'You gave me {bytes(decryption_fn(oracle, bytearray(c2), bytearray(c3)))}, but I expected {plaintext_padded[:16]}')
        return False

    print(f'All tests passed!\n\n{EXPLANATION_MSG}')
    return True
