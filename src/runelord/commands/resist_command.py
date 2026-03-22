import discord

from ..rq import AbilityScore
from .command import Command
from .. import render


class ResistCommand(Command):
    def __init__(self, ctx: discord.ApplicationContext):
        super().__init__(ctx)
        self.active = None
        self.passive = None
        self.label = None

    def arg_active(self, value: int):
        self.active = value

    def arg_passive(self, value: int):
        self.passive = value

    def arg_label(self, s: str):
        self.label = s

    def run(self) -> dict:
        effective = 50 + (self.active - self.passive) * 5
        ability = AbilityScore(effective)
        roll, result = ability.check()

        desc = ""
        desc += f"**{render.result_str(result)}:**"
        desc += f" {self.ctx.user.name} rolled **{render.roll_str(roll)}**"
        desc += f" against {effective} ({self.active} vs {self.passive})"
        if self.label:
            desc += f": _{self.label}_"
        desc += "."
        color = render.result_color(result)
        embed = discord.Embed(description=desc, color=color)
        return {"embed": embed}
