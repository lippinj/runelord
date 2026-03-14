import discord
from .rq import AbilityCheckResult


def result_str(result: AbilityCheckResult) -> str:
    return {
        AbilityCheckResult.CRITICAL: "Critical success",
        AbilityCheckResult.SPECIAL: "Special success",
        AbilityCheckResult.SUCCESS: "Success",
        AbilityCheckResult.FAILURE: "Failure",
        AbilityCheckResult.FUMBLE: "Fumble",
    }[result]


def result_color(result: AbilityCheckResult) -> discord.Color:
    return {
        AbilityCheckResult.CRITICAL: discord.Color.purple(),
        AbilityCheckResult.SPECIAL: discord.Color.blue(),
        AbilityCheckResult.SUCCESS: discord.Color.green(),
        AbilityCheckResult.FAILURE: discord.Color.light_gray(),
        AbilityCheckResult.FUMBLE: discord.Color.red(),
    }[result]


def roll_str(roll: int) -> str:
    if roll == 100:
        return "00"
    return str(roll)
