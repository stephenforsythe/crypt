"""
This is essentially a substitution cypher designed to avoid fequency analysis.

The idea is to shift the char to the right by an increasing number, until n = 25,
at which time the loop will start again.
Spaces are treated as a character at the end of the alphabet.
"""
import string


FULL_ALPHABET = string.lowercase + ' '
MOD_NUM = len(FULL_ALPHABET)


def encrypt_decrypt(instr, direction):
    shift = 0
    encrypted_message = ''

    for char in instr.lower():
        pos = string.index(FULL_ALPHABET, char)
        mod_pos = pos % MOD_NUM
        if direction == 'en':
            shift_pos = (mod_pos + shift) % MOD_NUM
        else:
            shift_pos = (mod_pos - shift) % MOD_NUM
        encrypted_message += FULL_ALPHABET[shift_pos]
        shift += 1

    return encrypted_message


eord = raw_input('Encrypt or decrypt? (e/d):\n')
if eord == 'e':
    user_input = raw_input('Message to be encrypted:\n')
    print 'encrypted message:\n'
    print encrypt_decrypt(user_input, 'en')
elif eord == 'd':
    user_input = raw_input('Message to be decrypted:\n')
    print 'plain text:\n'
    print encrypt_decrypt(user_input, 'de')
else:
    print 'error'
