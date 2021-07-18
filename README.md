# ComSSA Bot

This is the latest and greatest ComSSA Open-Source Discord Bot.

It is designed to be built with much more solid development practices from the beginning, and be open and available to anybody to view the source code, and contribute to the development if they'd like.

We hope to be able to create an example of good development practices, with Unit Testing, and automated Testing and Deployment using Docker.

The bot is developed using Python 3.9, although we will update this version as later versions of python become stable.

## Deployment:

This bot comes with a dockerfile that can be used to deploy the bot.

Alternately, the project can be cloned, and the dependencies installed with `python3 -m pip install -U pip && pip install -U -r requirements.txt`.

The bot will read the bot token to use from either the `--token` argument, or the `DISCORD_TOKEN` environment variable if the token argument isn't present.

To give the bot a discord bot token to connect to, create a bot account if you don't have one yet, a guide such as the one [here](https://discordpy.readthedocs.io/en/latest/discord.html) should explain the steps in detail.

The token can either be exported as environment variable `DISCORD_TOKEN`, or passed as argument `--token` when running the script.

The program is then runnable from the `src` directory with `python3 main.py`, or with `run.sh`.

If you would like to run the unit tests, they can be run with `python -m unittest discover -t src/ -s src/tests/`, or by running `test.sh`.
