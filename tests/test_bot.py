from unittest.mock import patch

import pytest

from tests.helpers import BotTester


@pytest.fixture
def tester():
    return BotTester()


@pytest.mark.asyncio
async def test_check_success(tester):
    with patch("runelord.rq.ability_score.d", return_value=42):
        response = await tester.rq.check(ability="50", label="")

    assert response.has_embed
    assert "JC Denton rolled" in response.embed.description
    assert "42" in response.embed.description


@pytest.mark.asyncio
async def test_check_with_label(tester):
    with patch("runelord.rq.ability_score.d", return_value=50):
        response = await tester.rq.check(ability="60", label="Climb")

    assert response.has_embed
    assert "JC Denton rolled" in response.embed.description
    assert "Climb" in response.embed.description


@pytest.mark.asyncio
async def test_check_invalid_ability(tester):
    response = await tester.rq.check(ability="fourteen", label="Oratory")

    assert response.has_embed
    assert response.is_error
