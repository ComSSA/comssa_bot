from discord.ext import commands
from datetime import datetime, timezone

class Example(commands.Cog):
    def __init__(self):
        # Init methods aren't necessary unless you want to initialise specific variables
        # They can also be used if you need an argument from the caller, such as bot
        self._start_time = datetime.now(timezone.utc)

    @commands.command()
    async def ping(self, ctx):
        """ping
        Responds "Pong! {time} seconds".
        time is the number of seconds to 2 decimal places between msg send and processing
        """
        # As this is a discord method, it is difficult to unit test, so usage
        # Should be kept to a minimum level
        time = self._time_between(ctx.message.created_at)
        await ctx.send(f"Pong! {time} seconds")
    
    @commands.command()
    async def uptime(self, ctx):
        """uptime
        Responds "Uptime: {time} seconds".
        Uptime is the time since this module was initialized.
        TODO: Implement a display to show times other than seconds.
        """
        time = self._time_between(self._start_time)
        await ctx.send(f"Uptime: {time} seconds")
    
    @staticmethod
    def _time_between(time_from: datetime) -> str:
        """time_between
        Arguments:
        time_from: datetime.datetime
            The time that we are calculating from.

        The function should return a string containing the time that has occured
        since time_from to the current time (given by datetime.now(timezone.utc)),
        in seconds, to two decimal places.
        """
        time_to = datetime.now(timezone.utc)
        # If the given time doesn't have a timezone, assume UTC
        # This prevents errors with mixing naive and aware datetime items
        if time_from.tzinfo is None:
            time_from = time_from.replace(tzinfo=timezone.utc)
        between = time_to - time_from
        between_seconds = f"{between.total_seconds():.2f}"
        return between_seconds