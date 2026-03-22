import functools

import discord

from ..error import Error, MultiError, UnhandledError


class Command:
    """Base class for bot commands."""

    def __init__(self, ctx: discord.ApplicationContext):
        self.ctx = ctx
        self._errors = []

    def add_error(self, error: Error):
        """Add an error to the list."""
        self._errors.append(error)

    def maybe_add_error(self, error: Error|None):
        """Add an error to the list, if not None."""
        if error:
            self.add_error(error)

    @property
    def has_error(self) -> bool:
        """Have there been one or more errors?"""
        return len(self._errors) > 0

    @property
    def consolidated_error(self) -> Error:
        """Return single error object (possibly a MultiError)."""
        if len(self._errors) > 1:
            return MultiError(self._errors)
        return self._errors[0]

    def run(self) -> dict:
        """Run the command and make the response."""
        raise NotImplementedError()

    async def run_or_fail(self) -> dict:
        """Run and make the response (handling errors)."""
        if self.has_error:
            return self.consolidated_error.as_response()
        try:
            return self.run()
        except Exception as exc:
            return UnhandledError(exc).as_response()

    async def run_and_respond(self, ctx: discord.ApplicationContext) -> dict:
        response = await self.run_or_fail()
        await ctx.respond(**response)

