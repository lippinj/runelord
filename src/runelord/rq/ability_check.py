from enum import Enum
from typing import NamedTuple


class AbilityCheckResult(Enum):
    """Result category of a check."""

    FUMBLE = -1
    FAILURE = 0
    SUCCESS = 1
    SPECIAL = 2
    CRITICAL = 3


class AbilityCheckThresholds(NamedTuple):
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
            return AbilityCheckResult.CRITICAL
        if roll <= self.special:
            return AbilityCheckResult.SPECIAL
        if roll <= self.success:
            return AbilityCheckResult.SUCCESS
        if roll >= self.fumble:
            return AbilityCheckResult.FUMBLE
        return AbilityCheckResult.FAILURE
