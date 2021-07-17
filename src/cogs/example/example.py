import discord
from discord.ext import commands
import asyncio
import concurrent.futures
from io import BytesIO
from datetime import datetime, timezone
from functools import partial
from typing import Optional, TYPE_CHECKING
import cogs.example.mandelbrot as mandelbrot

# Hack to make discord.py-stubs work properly, because for some reason it believes that Cog is generic, while in runtime it is not
if TYPE_CHECKING:
    Cog = commands.Cog[commands.Context]
else:
    Cog = commands.Cog

class Example(Cog):
    def __init__(self) -> None:
        # Init methods aren't necessary unless you want to initialise specific variables
        # They can also be used if you need an argument from the caller, such as bot
        self._start_time = datetime.now(timezone.utc)

    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        """ping
        Responds "Pong! {time} seconds".
        time is the number of seconds to 2 decimal places between msg send and processing
        """
        # As this is a discord method, it is difficult to unit test, so built-in logic
        # Should be kept to a minimum level
        time = self._time_between(ctx.message.created_at)
        await ctx.send(f"Pong! {time} seconds")
    
    @commands.command()
    async def uptime(self, ctx: commands.Context) -> None:
        """uptime
        Responds "Uptime: {time} seconds".
        Uptime is the time since this module was initialized.
        TODO: Implement a display to show times other than seconds.
        """
        time = self._time_between(self._start_time, ctx.message.created_at)
        await ctx.send(f"Uptime: {time} seconds")
    
    @commands.command()
    async def mandelbrot(self, ctx: commands.Context, resolution: int = 500):
        if resolution < 1:
            await ctx.send("Invalid resolution")
        elif resolution > 1000: #TODO: Implement config read
            await ctx.send("Resolution exceeds limit")
        else:
            # Valid resolution
            # Give a typing notification while this runs
            with ctx.typing():
                start_time = datetime.now()
                # Create an executor that will let this task be run in a different kernel thread
                with concurrent.futures.ProcessPoolExecutor() as pool:
                    loop = asyncio.get_running_loop()
                    to_run = partial(mandelbrot.generate_mandelbrot, resolution)
                    try:
                        result: bytes = await loop.run_in_executor(
                            pool, to_run
                        )
                        # Once has returned, can upload
                        file = discord.File(BytesIO(result), "mandelbrot.png")
                        end_time = datetime.now()
                        await ctx.send(f"Generated Mandelbrot in {self._time_between(start_time, end_time)} seconds", file=file)
                    except MemoryError:
                        await ctx.send(f"Error: Not enough memory")
    
    @staticmethod
    def _time_between(time_from: datetime, time_to: Optional[datetime] = None, places: int = 2) -> str:
        """time_between
        Arguments:
        time_from: datetime.datetime
            The time that we are calculating from.

        The function should return a string containing the time that has occurred
        since time_from to the current time (given by datetime.now(timezone.utc)),
        in seconds, to two decimal places.
        """
        # Get current time if not provided
        if time_to is None:
            time_to = datetime.now(timezone.utc)
        # If the given time doesn't have a timezone, assume UTC
        # This prevents errors with mixing naive and aware datetime items
        if time_from.tzinfo is None:
            time_from = time_from.replace(tzinfo=timezone.utc)

        if time_to.tzinfo is None:
            time_to = time_to.replace(tzinfo=timezone.utc)
        
        between = time_to - time_from
        between_seconds = f"{between.total_seconds():.{places}f}"
        return between_seconds