from unittest.mock import AsyncMock, MagicMock

import discord

from runelord.bot import create_bot


class ResponseTester:
    def __init__(self, response: dict):
        self.response = response

    @property
    def embed(self):
        return self.response["embed"]

    @property
    def has_embed(self):
        r = self.response
        return "embed" in r and isinstance(r["embed"], discord.Embed)

    @property
    def is_error(self):
        return self.embed.title == "Error"


class CommandProxy:
    def __init__(self, tester: "BotTester", group_name: str):
        self._tester = tester
        self._group_name = group_name

    def __getattr__(self, command_name: str):
        async def invoke(**kwargs):
            tester = self._tester
            cmd = tester._find_command(self._group_name, command_name)
            tester.ctx.respond.reset_mock()
            await cmd.callback(tester.ctx, **kwargs)
            tester.ctx.respond.assert_called_once()
            return ResponseTester(tester.ctx.respond.call_args[1])
        return invoke


class BotTester:
    def __init__(self):
        self.bot = create_bot()

        self.ctx = MagicMock()
        self.ctx.user.name = "JC Denton"
        self.ctx.respond = AsyncMock()

    def __getattr__(self, group_name: str):
        return CommandProxy(self, group_name)

    def _find_command(self, group_name, command_name):
        group = self._find_group(group_name)
        for cmd in group.walk_commands():
            if cmd.name == command_name:
                return cmd
        raise AssertionError(f"No command '{command_name}' in group '{group_name}'")

    def _find_group(self, group_name: str):
        for cmd in self.bot.pending_application_commands:
            if cmd.name == group_name:
                return cmd
        raise AssertionError(f"No group '{group_name}'")
