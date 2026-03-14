import discord

from ..parse import ParsedAbilityScore
from .command import Command
from .. import render


class CheckCommand(Command):
    def __init__(self, ctx: discord.ApplicationContext):
        super().__init__(ctx)
        self.ability = None
        self.label = None

    @Command.skip_on_error
    def arg_ability(self, s: str):
        self.ability = ParsedAbilityScore(s)
        self.error = self.ability.error

    @Command.skip_on_error
    def arg_label(self, s: str):
        self.label = s

    @Command.skip_on_error
    def run(self):
        roll, result = self.ability.check()
        desc = ""
        desc += f"**{render.result_str(result)}:**"
        desc += f" {self.ctx.user.name} rolled **{render.roll_str(roll)}**"
        desc += f" against {self.ability.render()}"
        if self.label:
            desc += f": _{self.label}_"
        desc += "."
        color = render.result_color(result)
        self.response["embed"] = discord.Embed(description=desc, color=color)
