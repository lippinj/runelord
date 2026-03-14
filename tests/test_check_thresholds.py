from runelord.check import Result, Thresholds


def test_classification_1():
    t = Thresholds(1, 1, 5, 96)
    assert t.classify(1) == Result.CRITICAL
    assert t.classify(2) == Result.SUCCESS
    # ...
    assert t.classify(5) == Result.SUCCESS
    assert t.classify(6) == Result.FAILURE
    # ...
    assert t.classify(95) == Result.FAILURE
    assert t.classify(96) == Result.FUMBLE
    # ...
    assert t.classify(100) == Result.FUMBLE


def test_classification_68():
    t = Thresholds(3, 14, 68, 99)
    assert t.classify(1) == Result.CRITICAL
    # ...
    assert t.classify(3) == Result.CRITICAL
    assert t.classify(4) == Result.SPECIAL
    # ...
    assert t.classify(14) == Result.SPECIAL
    assert t.classify(15) == Result.SUCCESS
    # ...
    assert t.classify(68) == Result.SUCCESS
    assert t.classify(69) == Result.FAILURE
    # ...
    assert t.classify(98) == Result.FAILURE
    assert t.classify(99) == Result.FUMBLE
    assert t.classify(100) == Result.FUMBLE


def test_classification_100():
    t = Thresholds(5, 20, 95, 100)
    assert t.classify(1) == Result.CRITICAL
    # ...
    assert t.classify(5) == Result.CRITICAL
    assert t.classify(6) == Result.SPECIAL
    # ...
    assert t.classify(20) == Result.SPECIAL
    assert t.classify(21) == Result.SUCCESS
    # ...
    assert t.classify(95) == Result.SUCCESS
    assert t.classify(96) == Result.FAILURE
    # ...
    assert t.classify(99) == Result.FAILURE
    assert t.classify(100) == Result.FUMBLE
