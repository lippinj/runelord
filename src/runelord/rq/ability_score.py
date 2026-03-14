from ..dice import d
from .ability_check import AbilityCheckThresholds
from .util import clamp


class AbilityScore:
    """Ability score, for checks."""

    def __init__(self, score: int):
        self.score = score

        # Percent probabilities of:
        p_success = clamp(score, 5, 95)
        p_special = clamp(round(score / 5), 1, 95)
        p_critical = clamp(round(score / 20), 1, 95)
        p_failure = 100 - p_success
        p_fumble = clamp(round(p_failure / 20), 1, 95)

        # Corresponding thresholds:
        th_fumble = 101 - p_fumble
        self.thresholds = AbilityCheckThresholds.create(
            p_critical, p_special, p_success, th_fumble
        )

    def check(self, roll: int | None = None):
        """Roll against this ability and return (roll, result)."""
        if roll is None:
            roll = d(100)
        assert roll in range(1, 101)
        return roll, self.thresholds.classify(roll)
