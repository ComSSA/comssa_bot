# Contributing Guide:

This bot is developed by ComSSA, for ComSSA, and we welcome any members who would like to add new features, practice skills, or learn entirely new ones.

Se the issues page for current bugs or minor improvements, or the planned features section for ideas that we would like to begin working on.

## Development:

To work on the bot, you'll need to setup a development environment.

First, either clone the repository with `git clone https://github.com/ComSSA/comssa_bot`, or fork a copy of the repo so that you can directly push changes there, and then clone this locally.

Then, ensure that the latest version of Python 3.9 is installed. This can be done either from [python.org](https://www.python.org/downloads/), your distrobutions repositories (Note that repositories often do not have the latest version of Python), or through [pyenv](https://github.com/pyenv/pyenv), in addition to other alternate python managers.

### Dependancies

Next, you must install the libraries dependancies. As we specify specific versions of these libraries, to ensure that there are no issues from differing, untested versions of libraries, it may be preferrable to not install these on your local machine if you have other projects with their own dependancies.

If you are comfortable using your own system, you may skip to the next paragraph. If you would like to keep the depedancies seperate, you can setup a new Virtual Environment using Python's built in system, [venv](https://docs.python.org/3/tutorial/venv.html), or with pyenv's manager if you used that from [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv). (Note that this plugin comes installed by default if you followed the standard installation steps, so you can skip past the installation steps).

Once you have setup your environment, you can install the dependancies with `python3 -m pip install -U pip && python3 -m pip install -U -r requirements.txt`, which will update pip and then download and install other python dependancies.

### Running

The program can then be locally run or tested as specified in the README.

## Development Rules:

TODO: Finish this
