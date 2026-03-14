import os


def d(n: int):
    """Roll an n-sided die (returns a value between 1 and n)."""
    assert n >= 1
    i = int.from_bytes(os.urandom(4), "little")
    return (i % n) + 1
