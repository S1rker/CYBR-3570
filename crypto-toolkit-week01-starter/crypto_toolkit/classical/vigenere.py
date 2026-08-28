"""
Module: crypto_toolkit.classical.vigenere

Educational implementation of the Vigenere cipher.

WARNING: This module is for learning only. Do not use the Vigenere cipher
to protect real information.
"""
import caesar
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def char_to_num(ch: str) -> int:
    """Convert uppercase A-Z to a number 0-25."""
    return ALPHABET.index(ch)


def num_to_char(n: int) -> str:
    """Convert an integer to uppercase A-Z using modulo 26."""
    return ALPHABET[n % 26]


def vigenere_encrypt(plaintext: str, keyword: str) -> str:
    """Encrypt plaintext with a Vigenere cipher."""
    coded_message = ''
    for spot in range(len(plaintext)):
        letter = plaintext[spot]
        keylength = len(keyword)
        key = ALPHABET.index(keyword[spot % keylength].upper())
        coded_message = coded_message + caesar.caesar_encrypt(letter, key)

    return coded_message


def vigenere_decrypt(ciphertext: str, keyword: str) -> str:
    """Decrypt Vigenere ciphertext with a known shift."""   
    plain_message = ''
    for spot in range(len(ciphertext)):
        letter = ciphertext[spot]
        keylength = len(keyword)
        key = ALPHABET.index(keyword[spot % keylength].upper())
        plain_message = plain_message + caesar.caesar_decrypt(letter, key)

    return plain_message


def vigenere_analysis(ciphertext: str) -> list[tuple[int, str]]:
    """Return analysis of various lengths of passphrase"""
    # TODO: Implement in Lab 01.
    raise NotImplementedError

thing = vigenere_encrypt("words many words", "keyword")
print(vigenere_decrypt(thing, 'keyword'))