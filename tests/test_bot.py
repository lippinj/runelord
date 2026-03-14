from unittest.mock import AsyncMock, MagicMock, patch

import discord
import pytest

from runelord.bot import create_bot


@pytest.fixture
def bot():
    return create_bot()


def find_group(bot, group_name):
    for cmd in bot.pending_application_commands:
        if cmd.name == group_name:
            return cmd
    raise AssertionError(f"No command group '{group_name}'")


def find_group_command(group, command_name):
    for cmd in group.walk_commands():
        if cmd.name == command_name:
            return cmd
    raise AssertionError(f"No command '{command_name}'")


def find_command(bot, group_name, command_name):
    return find_group_command(find_group(bot, group_name), command_name)


def mock_ctx():
    ctx = MagicMock()
    ctx.user.name = "JC Denton"
    ctx.respond = AsyncMock()
    return ctx


@pytest.mark.asyncio
async def test_check_success(bot):
    ctx = mock_ctx()
    cmd = find_command(bot, "rq", "check")

    with patch("runelord.rq.ability_score.d", return_value=42):
        await cmd.callback(ctx, ability="50", label="")

    ctx.respond.assert_called_once()
    _, kwargs = ctx.respond.call_args
    assert "embed" in kwargs
    embed = kwargs["embed"]
    assert isinstance(embed, discord.Embed)
    assert "JC Denton rolled" in embed.description
    assert "42" in embed.description


@pytest.mark.asyncio
async def test_check_with_label(bot):
    ctx = mock_ctx()
    cmd = find_command(bot, "rq", "check")

    with patch("runelord.rq.ability_score.d", return_value=50):
        await cmd.callback(ctx, ability="60", label="Climb")

    _, kwargs = ctx.respond.call_args
    embed = kwargs["embed"]
    assert "JC Denton rolled" in embed.description
    assert "Climb" in embed.description


@pytest.mark.asyncio
async def test_check_invalid_ability(bot):
    ctx = mock_ctx()
    cmd = find_command(bot, "rq", "check")

    await cmd.callback(ctx, ability="not_valid", label="")

    ctx.respond.assert_called_once()
    response_text = ctx.respond.call_args[0][0]
    assert "Error" in response_text
