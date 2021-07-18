# Contributing Guide:

This bot is developed by ComSSA, for ComSSA, and we welcome any members who would like to add new features, practice skills, or learn entirely new ones.

Se the issues page for current bugs or minor improvements, or the planned features section for ideas that we would like to begin working on.

## Development:

To work on the bot, you'll need to setup a development environment.

First, either clone the repository with `git clone https://github.com/ComSSA/comssa_bot`, or fork a copy of the repo so that you can directly push changes there, and then clone this locally.

You may either follow the below steps, or use docker to build an image to run the bot from.

Then, ensure that the latest version of Python 3.9 is installed. This can be done either from [python.org](https://www.python.org/downloads/), your distrobutions repositories (Note that repositories often do not have the latest version of Python), or through [pyenv](https://github.com/pyenv/pyenv), in addition to other alternate python managers.

### Dependencies

Next, you must install the libraries dependencies. As we specify specific versions of these libraries, to ensure that there are no issues from differing, untested versions of libraries, it may be preferable to not install these on your local machine if you have other projects with their own dependencies.

If you are comfortable using your own system, you may skip to the next paragraph. If you would like to keep the dependencies separate, you can setup a new Virtual Environment using Python's built in system, [venv](https://docs.python.org/3/tutorial/venv.html), or with pyenv's manager if you used that from [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv). (Note that this plugin comes installed by default if you followed the standard installation steps, so you can skip past the installation steps).

The debian names of the required software can be found in `dependencies.txt`, and installed with `sudo xargs -a dependencies.txt -r apt-get install -y`.

Once you have setup your environment, you can install the dependencies with `python3 -m pip install -U pip && python3 -m pip install -U -r requirements.txt`, which will update pip and then download and install other python dependencies.

### Running

The program can then be locally run or tested as specified in the README.

## Development Rules:

Each different 'Module' of the bot, which is divided by specific functionality, should be placed in a new folder inside the `cogs` folder.

Please try to keep functionality that directly works with the Discord API inside the command function, and place other functionality inside other commands, so that they can be unit tested, as unit testing with the Discord API itself is complicated and can result in more issues than it fixes.

Try to make good unit tests that verify that each non-discord-api function works correctly and as expected.

`mypy` is used to check type safety and try to avoid issues with unexpected type problems or edge cases. It can be run from the `src/` directory with `mypy main.py`. Configuration is stored in `src/mypy.ini`. Unfortunately there is no type checker that can handle Cython .pyx files properly as well at the moment, so currently these failed imports are ignored.

Unit testing of C source files is planned but not yet added as the best way to implement testing is determined.
