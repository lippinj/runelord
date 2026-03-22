import discord


class Error:
    """Generic error encountered while processing a command."""

    COLOR = discord.Color.red()

    def as_md(self) -> str:
        return "An error occurred."

    def as_embed(self) -> discord.Embed:
        """Build single-error embed."""
        embed = discord.Embed(title="Error", color=Error.COLOR)
        self.populate_embed(embed)
        return embed

    def as_response(self) -> dict:
        """Build response dict."""
        return {
            "embed": self.as_embed(),
            "ephemeral": True,
        }

    def populate_embed(self, embed: discord.Embed):
        """Add error information to an embed."""
        if embed.description:
            embed.description += "\n"
        else:
            embed.description = ""
        embed.description += self.as_md()


class UnhandledError(Error):
    """Unhandled error (uncaught Python exception)."""

    def __init__(self, exception: Exception):
        self.exception = exception

    def as_md(self) -> str:
        s = "Unexpected internal error (unhandled exception). Details:"
        s += "\n\n"
        s += f"```\n{self.exception}\n```"
        return s


class MultiError(Error):
    """Several errors in a single command."""

    def __init__(self, errors: list[Error]):
        self.errors = errors

    def as_md(self) -> str:
        return "\n\n".join(error.as_md() for error in self.errors)

    def as_embed(self):
        title = f"{len(self.errors)} errors"
        embed = discord.Embed(title=title, color=Error.COLOR)
        for error in self.errors:
            error.populate_embed(embed)
        return embed
