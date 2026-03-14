from enum import Enum
from typing import NamedTuple

from .random import d100


class Result(Enum):
    """Result category of a check."""
    FUMBLE = -1
    FAILURE = 0
    SUCCESS = 1
    SPECIAL = 2
    CRITICAL = 3


class Thresholds(NamedTuple):
    """Result thresholds."""
    critical: int
    special: int
    success: int
    fumble: int

    @classmethod
    def create(cls, critical: int, special: int, success: int, fumble: int):
        is_sorted = lambda x: sorted(x) == x
        assert is_sorted([critical, special, success, fumble])
        assert critical >= 1
        assert fumble <= 100
        return cls(critical, special, success, fumble)

    def classify(self, roll: int):
        assert roll in range(1, 101)
        if roll <= self.critical:
            return Result.CRITICAL
        if roll <= self.special:
            return Result.SPECIAL
        if roll <= self.success:
            return Result.SUCCESS
        if roll >= self.fumble:
            return Result.FUMBLE
        return Result.FAILURE


class Ability:
    """Ability score, for checks."""

    def __init__(self, score: int):
        self.score = score

        # Percent probabilities of:
        pcr = max(round(score / 20), 1) # crit
        psp = max(round(score / 5), 1)  # special
        psu = max(min(score, 95), 5)    # success
        pfa = 100 - psu                 # failure
        pfu = max(round(pfa / 20), 1)   # fumble

        # Corresponding thresholds:
        self.thresholds = Thresholds.create(pcr, psp, psu, 101 - pfu)

    def check(self, roll: int):
        return self.thresholds.classify(roll)


class Check:
    """Ability check."""

    def __init__(self, ability: Ability, roll: int | None = None):
        roll = roll if (roll is not None) else d100()
        assert roll in range(1, 101)
        self.roll = roll
        self.ability = ability
        self.result = ability.check(roll)
