from .rq import AbilityScore

import d20


class ParsedAbilityScore:
    def __init__(self, raw: str):
        self.raw = raw
        self.error = self.parse()

    def parse(self):
        if "d" in self.raw:
            return ParsedAbilityScore.ErrDiceRoll()
        try:
            self.roll = d20.roll(self.raw)
            self.ability = AbilityScore(self.roll.total)
        except d20.RollSyntaxError as e:
            return ParsedAbilityScore.ErrSyntax(e)
        return None

    @property
    def is_literal(self):
        ast = self.roll.ast.children
        return len(ast) == 1 and type(ast[0]) == d20.diceast.Literal

    def render(self):
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

    @staticmethod
    def ErrDiceRoll():
        return "Ability score cannot contain a dice roll."

    @staticmethod
    def ErrSyntax(e: d20.RollSyntaxError):
        return f"Syntax error in ability score formula: {e}"
