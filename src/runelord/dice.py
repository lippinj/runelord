import secrets


def d(n: int):
    """Roll an n-sided die (returns a value between 1 and n)."""
    assert n >= 1
    return secrets.randbelow(n) + 1
