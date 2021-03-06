FROM python:3.9-buster

WORKDIR /app

# Pass each line in dependencies.txt as an argument to apt-get install, to attempt to install each package
# xargs required as apt-get and apt don't offer file reading functionality
COPY dependencies.txt dependencies.txt
RUN apt-get update && xargs -a dependencies.txt -r apt-get install -y

# Install each required python package in requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src/ src

WORKDIR src
# Build Cython files
RUN python setup.py build_ext --inplace

# Run unit tests, if this fails build will fail
RUN python -m unittest discover -s tests/

RUN mypy main.py

CMD [ "python", "main.py" ]
