'''
Educational block cipher helper functions for CYBR 3570.

WARNING:
These helpers are for learning and demonstration. Do not use this module as a
complete production encryption library.
'''


import hashlib
import secrets

def xor_bytes(a: bytes, b: bytes) -> bytes:
    """Return the bytewise XOR of two equal-length byte strings."""
    if len(a) != len(b):
        raise ValueError("Inputs must have the same length")
    return bytes(x ^ y for x, y in zip(a, b))



def toy_keystream(key: bytes, nonce: bytes, length: int) -> bytes:
    """Generate a toy keystream using SHA-256(key || nonce || counter)."""
    output = bytearray()
    counter = 0
    while len(output) < length:
        block = hashlib.sha256(
            key + nonce + counter.to_bytes(8, "big")
        ).digest()
        output.extend(block)
        counter += 1
    return bytes(output[:length])



def toy_stream_encrypt(key: bytes, nonce: bytes, plaintext: bytes) -> bytes:
    ks = toy_keystream(key, nonce, len(plaintext))
    return xor_bytes(plaintext, ks)



def detect_keystream_reuse(c1: bytes, c2: bytes) -> bytes:
    """Return c1 XOR c2 to expose keystream reuse."""
    return xor_bytes(c1, c2)