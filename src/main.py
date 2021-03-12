import sys, os, argparse
import discord
from discord.ext import commands
from Cogs import example

bot = commands.Bot(
    command_prefix=".",
    case_insensitive=True
)

def main():
    """main
    Main is defined as it's own function so that it will only run if the file is run directly.
    This prevents the script from running if you decide to import the file.
    It also means that we can safely define methods later in the code and call them,
    as they will be defined by the time this method is run.
    At the end of this file is an if statement deciding if this method should be run.
    """
    # First, getting config data
    # TODO: Create a serperate library for this task
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--token",
        help="The Discord Bot Token to connect to. If not given, will attempt to read from $DISCORD_TOKEN",
        required=False
    )

    args = parser.parse_args()

    if args.token:
        token = args.token
    else:
        token = os.environ.get("DISCORD_TOKEN")
    if token is None:
        print("Error: No discord bot token specified.", file=sys.stderr)
        sys.exit(1)
    
    start_bot(token)

# Start up bot with given token
def start_bot(token):
    bot.add_cog(example.Example())

    try:
        bot.run(token)
    except discord.LoginFailure:
        print("Login error, please set a valid key")
        sys.exit(1)

@bot.event
async def on_ready():
    # Runs when the bot successfully starts
    print(f"Logged in as {bot.user}")

# Run main() if this file is being run directly and not imported
if __name__ == "__main__":
    main()