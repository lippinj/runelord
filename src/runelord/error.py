import discord


class Error:
    def make_title(self, ctx: discord.ApplicationContext) -> str:
        return "Error"

    def make_description(self, ctx: discord.ApplicationContext) -> str:
        return "An error occurred."

    def make_embed(self, ctx: discord.ApplicationContext) -> discord.Embed:
        return discord.Embed(
            title=self.make_title(ctx),
            description=self.make_description(ctx),
            color=discord.Color.red(),
        )

    def make_response(self, ctx: discord.ApplicationContext) -> dict:
        return {
            "embed": self.make_embed(ctx),
            "ephemeral": True,
        }


class UnexpectedError(Error):
    def __init__(self, e):
        self.e = e

    def make_title(self, ctx: discord.ApplicationContext) -> str:
        return "Internal Error"

    def make_description(self, ctx: discord.ApplicationContext) -> str:
        return f"The bot made a boo-boo. Tell the developer:\n{self.e}"
