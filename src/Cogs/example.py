from discord.ext import commands
import datetime import datetime, timezone

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
        time = self.ping_time(ctx.message.created_at)
        await ctx.send(f"Pong! {time} seconds")
    
    def ping_time(self, time_from):
        """ping_time
        Arguments:
        time_from: datetime.datetime
            The time that we are calculating from.

        The function should return a string containing the time that has occured since time_from,
        in seconds, to two decimal places.
        """
        time_to = datetime.now(timezone.utc)
        between = time_to - time_from
        between_seconds = f"{between.total_seconds():.2f}"
        return between_seconds