from discord.ext import commands


class Ping(commands.Cog, name="Ping Cog"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("WeebBot.cogs.ping.cog.py has been loaded!")

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Checks for a response from the bot"""
        await ctx.send("Pong")


def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))
