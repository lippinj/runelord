import discord

from .commands.augment_command import AugmentCommand
from .commands.check_command import CheckCommand
from .commands.resist_command import ResistCommand


def create_bot() -> discord.Bot:
    bot = discord.Bot()

    guild_ids = []
    rq = bot.create_group("rq", "Runelord commands")

    @rq.command(description="Roll an ordinary ability check.")
    @discord.option("ability", type=str, description="Ability score")
    @discord.option("label", type=str, description="Text description", default="")
    async def check(ctx: discord.ApplicationContext, ability: str, label: str):
        cmd = CheckCommand(ctx)
        cmd.arg_ability(ability)
        cmd.arg_label(label)
        await cmd.run_respond()

    @rq.command(description="Roll an augment check.")
    @discord.option("ability", type=str, description="Ability score")
    @discord.option("label", type=str, description="Text description", default="")
    async def augment(ctx: discord.ApplicationContext, ability: str, label: str):
        cmd = AugmentCommand(ctx)
        cmd.arg_ability(ability)
        cmd.arg_label(label)
        await cmd.run_respond()

    @rq.command(description="Roll a check on the resistance table.")
    @discord.option("active", type=int, description="Active characteristic")
    @discord.option("passive", type=int, description="Passive characteristic")
    @discord.option("label", type=str, description="Text description", default="")
    async def resist(
        ctx: discord.ApplicationContext, active: int, passive: int, label: str
    ):
        cmd = ResistCommand(ctx)
        cmd.arg_active(active)
        cmd.arg_passive(passive)
        cmd.arg_label(label)
        await cmd.run_respond()

    return bot
