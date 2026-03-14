import os


def d100():
    """Random number between 1 and 100."""
    return int(os.urandom(4), "little") % 100 + 1
