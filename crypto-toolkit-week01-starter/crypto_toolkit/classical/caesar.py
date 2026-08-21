"""
Module: crypto_toolkit.classical.caesar

Educational implementation of the Caesar cipher.

WARNING: This module is for learning only. Do not use the Caesar cipher
to protect real information.
"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def char_to_num(ch: str) -> int:
    """Convert uppercase A-Z to a number 0-25."""
    return ALPHABET.index(ch)


def num_to_char(n: int) -> str:
    """Convert an integer to uppercase A-Z using modulo 26."""
    return ALPHABET[n % 26]


def caesar_encrypt(plaintext: str, shift: int) -> str:
    """Encrypt plaintext with a Caesar shift."""
    # TODO: Implement in Lab 01.
    raise NotImplementedError


def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """Decrypt Caesar ciphertext with a known shift."""
    # TODO: Implement in Lab 01.
    raise NotImplementedError


def brute_force_caesar(ciphertext: str) -> list[tuple[int, str]]:
    """Return all possible Caesar decryptions."""
    # TODO: Implement in Lab 01.
    raise NotImplementedError
