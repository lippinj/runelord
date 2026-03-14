from runelord.rq import AbilityCheckResult, AbilityCheckThresholds


def test_classify_low_skill():
    t = AbilityCheckThresholds(1, 1, 5, 96)
    assert t.classify(1) == AbilityCheckResult.CRITICAL
    assert t.classify(2) == AbilityCheckResult.SUCCESS
    # ...
    assert t.classify(5) == AbilityCheckResult.SUCCESS
    assert t.classify(6) == AbilityCheckResult.FAILURE
    # ...
    assert t.classify(95) == AbilityCheckResult.FAILURE
    assert t.classify(96) == AbilityCheckResult.FUMBLE
    # ...
    assert t.classify(100) == AbilityCheckResult.FUMBLE


def test_classify_mid_skill():
    t = AbilityCheckThresholds(3, 14, 68, 99)
    assert t.classify(1) == AbilityCheckResult.CRITICAL
    # ...
    assert t.classify(3) == AbilityCheckResult.CRITICAL
    assert t.classify(4) == AbilityCheckResult.SPECIAL
    # ...
    assert t.classify(14) == AbilityCheckResult.SPECIAL
    assert t.classify(15) == AbilityCheckResult.SUCCESS
    # ...
    assert t.classify(68) == AbilityCheckResult.SUCCESS
    assert t.classify(69) == AbilityCheckResult.FAILURE
    # ...
    assert t.classify(98) == AbilityCheckResult.FAILURE
    assert t.classify(99) == AbilityCheckResult.FUMBLE
    assert t.classify(100) == AbilityCheckResult.FUMBLE


def test_classify_high_skill():
    t = AbilityCheckThresholds(5, 20, 95, 100)
    assert t.classify(1) == AbilityCheckResult.CRITICAL
    # ...
    assert t.classify(5) == AbilityCheckResult.CRITICAL
    assert t.classify(6) == AbilityCheckResult.SPECIAL
    # ...
    assert t.classify(20) == AbilityCheckResult.SPECIAL
    assert t.classify(21) == AbilityCheckResult.SUCCESS
    # ...
    assert t.classify(95) == AbilityCheckResult.SUCCESS
    assert t.classify(96) == AbilityCheckResult.FAILURE
    # ...
    assert t.classify(99) == AbilityCheckResult.FAILURE
    assert t.classify(100) == AbilityCheckResult.FUMBLE
