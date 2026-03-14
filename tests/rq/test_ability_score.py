from runelord.rq import AbilityCheckThresholds, AbilityScore


def test_score_to_thresholds():
    assert AbilityScore(1).thresholds == AbilityCheckThresholds(1, 1, 5, 96)
    assert AbilityScore(2).thresholds == AbilityCheckThresholds(1, 1, 5, 96)
    assert AbilityScore(3).thresholds == AbilityCheckThresholds(1, 1, 5, 96)
    assert AbilityScore(4).thresholds == AbilityCheckThresholds(1, 1, 5, 96)
    assert AbilityScore(5).thresholds == AbilityCheckThresholds(1, 1, 5, 96)
    assert AbilityScore(6).thresholds == AbilityCheckThresholds(1, 1, 6, 96)
    assert AbilityScore(7).thresholds == AbilityCheckThresholds(1, 1, 7, 96)
    assert AbilityScore(8).thresholds == AbilityCheckThresholds(1, 2, 8, 96)
    assert AbilityScore(9).thresholds == AbilityCheckThresholds(1, 2, 9, 96)
    # ...
    assert AbilityScore(28).thresholds == AbilityCheckThresholds(1, 6, 28, 97)
    assert AbilityScore(29).thresholds == AbilityCheckThresholds(1, 6, 29, 97)
    assert AbilityScore(30).thresholds == AbilityCheckThresholds(2, 6, 30, 97)
    assert AbilityScore(31).thresholds == AbilityCheckThresholds(2, 6, 31, 98)
    assert AbilityScore(32).thresholds == AbilityCheckThresholds(2, 6, 32, 98)
    assert AbilityScore(33).thresholds == AbilityCheckThresholds(2, 7, 33, 98)
    # ...
    assert AbilityScore(94).thresholds == AbilityCheckThresholds(5, 19, 94, 100)
    assert AbilityScore(95).thresholds == AbilityCheckThresholds(5, 19, 95, 100)
    assert AbilityScore(96).thresholds == AbilityCheckThresholds(5, 19, 95, 100)
    assert AbilityScore(97).thresholds == AbilityCheckThresholds(5, 19, 95, 100)
    assert AbilityScore(98).thresholds == AbilityCheckThresholds(5, 20, 95, 100)
    assert AbilityScore(99).thresholds == AbilityCheckThresholds(5, 20, 95, 100)
    assert AbilityScore(100).thresholds == AbilityCheckThresholds(5, 20, 95, 100)
    assert AbilityScore(101).thresholds == AbilityCheckThresholds(5, 20, 95, 100)
    assert AbilityScore(102).thresholds == AbilityCheckThresholds(5, 20, 95, 100)
    assert AbilityScore(103).thresholds == AbilityCheckThresholds(5, 21, 95, 100)
    # ...
    assert AbilityScore(117).thresholds == AbilityCheckThresholds(6, 23, 95, 100)
    assert AbilityScore(118).thresholds == AbilityCheckThresholds(6, 24, 95, 100)
    assert AbilityScore(119).thresholds == AbilityCheckThresholds(6, 24, 95, 100)
    assert AbilityScore(120).thresholds == AbilityCheckThresholds(6, 24, 95, 100)
    assert AbilityScore(121).thresholds == AbilityCheckThresholds(6, 24, 95, 100)
    assert AbilityScore(122).thresholds == AbilityCheckThresholds(6, 24, 95, 100)
    # ...


def test_score_clamps_low():
    assert AbilityScore(0).thresholds == AbilityCheckThresholds(1, 1, 5, 96)
    assert AbilityScore(-1).thresholds == AbilityCheckThresholds(1, 1, 5, 96)
    assert AbilityScore(-100).thresholds == AbilityCheckThresholds(1, 1, 5, 96)
    assert AbilityScore(-1000).thresholds == AbilityCheckThresholds(1, 1, 5, 96)


def test_score_clamps_high():
    assert AbilityScore(200).thresholds == AbilityCheckThresholds(10, 40, 95, 100)
    assert AbilityScore(1000).thresholds == AbilityCheckThresholds(50, 95, 95, 100)
    assert AbilityScore(2000).thresholds == AbilityCheckThresholds(95, 95, 95, 100)
