from .error import Error
from .rq import AbilityScore

import d20
import discord


class ParsedAbilityScore:
    def __init__(self, raw: str):
        self.raw = raw
        self.error = self.parse()

    def parse(self):
        if "d" in self.raw:
            return self.ErrorDiceInFormula(self.raw)
        try:
            self.roll = d20.roll(self.raw)
            self.ability = AbilityScore(self.roll.total)
        except d20.RollSyntaxError as e:
            return self.ErrorBadFormula(self.raw, e)
        return None

    @property
    def is_literal(self):
        if self.error:
            return False
        ast = self.roll.ast.children
        return len(ast) == 1 and type(ast[0]) == d20.diceast.Literal

    def render(self):
        if self.error:
            return self.raw
        if self.is_literal:
            return str(self.score)
        else:
            expr = str(self.roll.ast)
            return f"{self.score} [{expr}]"

    @property
    def score(self):
        return self.ability.score

    def check(self, roll=None):
        return self.ability.check(roll)


    class ErrorDiceInFormula(Error):
        def __init__(self, expression: str):
            self.expression = expression

        def make_md(self):
            desc = ""
            desc += f"Not a valid ability score:\n"
            desc += f"> {self.expression}\n"
            desc += "The ability score cannot contain dice rolls."
            return desc


    class ErrorBadFormula(Error):
        def __init__(self, expression:str, e: d20.RollSyntaxError):
            self.expression = expression
            self.e = e

        def make_md(self):
            desc = ""
            desc += f"Not a valid ability score:\n"
            desc += f"> {self.expression}\n"
            desc += f"Must be a number or formula."
            return desc

        def populate_embed(self, embed: discord.Embed):
            embed.add_field(name="Example (number)", value="`60`", inline=True)
            embed.add_field(name="Example (formula)", value="`45 + 20`", inline=True)
            embed.add_field(name="Example (formula)", value="`50/2 + 15`", inline=True)
            embed.set_footer(text=f"Parse error: {self.e}")
