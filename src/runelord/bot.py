import discord

from .commands.check_command import CheckCommand


def create_bot() -> discord.Bot:
    bot = discord.Bot()

    guild_ids = [1482131624547193113]
    rq = bot.create_group("rq", "Runelord commands", guild_ids=guild_ids)

    @rq.command(description="Roll an ability check.")
    @discord.option("ability", type=str, description="Ability score expression")
    @discord.option("label", type=str, description="Label for the check", default="")
    async def check(ctx: discord.ApplicationContext, ability: str, label: str):
        cmd = CheckCommand(ctx)
        cmd.arg_ability(ability)
        cmd.arg_label(label)
        await cmd.run_respond()

    return bot
