from runelord.check import Ability, Thresholds


def test_ability_thresholds():
    assert Ability(1).thresholds == Thresholds(1, 1, 5, 96)
    assert Ability(2).thresholds == Thresholds(1, 1, 5, 96)
    assert Ability(3).thresholds == Thresholds(1, 1, 5, 96)
    assert Ability(4).thresholds == Thresholds(1, 1, 5, 96)
    assert Ability(5).thresholds == Thresholds(1, 1, 5, 96)
    assert Ability(6).thresholds == Thresholds(1, 1, 6, 96)
    assert Ability(7).thresholds == Thresholds(1, 1, 7, 96)
    assert Ability(8).thresholds == Thresholds(1, 2, 8, 96)
    assert Ability(9).thresholds == Thresholds(1, 2, 9, 96)
    # ...
    assert Ability(28).thresholds == Thresholds(1, 6, 28, 97)
    assert Ability(29).thresholds == Thresholds(1, 6, 29, 97)
    assert Ability(30).thresholds == Thresholds(2, 6, 30, 97)
    assert Ability(31).thresholds == Thresholds(2, 6, 31, 98)
    assert Ability(32).thresholds == Thresholds(2, 6, 32, 98)
    assert Ability(33).thresholds == Thresholds(2, 7, 33, 98)
    # ...
    assert Ability(94).thresholds == Thresholds(5, 19, 94, 100)
    assert Ability(95).thresholds == Thresholds(5, 19, 95, 100)
    assert Ability(96).thresholds == Thresholds(5, 19, 95, 100)
    assert Ability(97).thresholds == Thresholds(5, 19, 95, 100)
    assert Ability(98).thresholds == Thresholds(5, 20, 95, 100)
    assert Ability(99).thresholds == Thresholds(5, 20, 95, 100)
    assert Ability(100).thresholds == Thresholds(5, 20, 95, 100)
    assert Ability(101).thresholds == Thresholds(5, 20, 95, 100)
    assert Ability(102).thresholds == Thresholds(5, 20, 95, 100)
    assert Ability(103).thresholds == Thresholds(5, 21, 95, 100)
    # ...
    assert Ability(117).thresholds == Thresholds(6, 23, 95, 100)
    assert Ability(118).thresholds == Thresholds(6, 24, 95, 100)
    assert Ability(119).thresholds == Thresholds(6, 24, 95, 100)
    assert Ability(120).thresholds == Thresholds(6, 24, 95, 100)
    assert Ability(121).thresholds == Thresholds(6, 24, 95, 100)
    assert Ability(122).thresholds == Thresholds(6, 24, 95, 100)
    # ...
