import functools

import discord

from ..error import UnexpectedError


class Command:
    """Base class for bot commands."""

    def __init__(self, ctx: discord.ApplicationContext):
        self.ctx = ctx
        self.error = None
        self.response = {}

    @staticmethod
    def skip_on_error(f):
        """Skip method if an error has already occurred."""

        @functools.wraps(f)
        def wrapped(self, *args, **kwargs):
            if self.error:
                return
            return f(self, *args, **kwargs)

        return wrapped

    def run(self):
        raise NotImplementedError()

    async def respond(self):
        """Send the error or response to Discord."""
        if self.error:
            await self.ctx.respond(**self.error.make_response(self.ctx))
        else:
            await self.ctx.respond(**self.response)

    async def run_respond(self):
        """Run the command and send the response, catching unexpected errors."""
        try:
            self.run()
        except Exception as e:
            self.error = UnexpectedError(e)
        await self.respond()
