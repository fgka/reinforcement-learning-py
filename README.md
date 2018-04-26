# Credits

First and foremost, this is a tentative to _pythonize_ the code in [dbatalov/reinforcement-learning](https://github.com/dbatalov/reinforcement-learning).

# Requirements

You need to have the following:
* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [pip](https://pypi.org/project/pip/) (obviously compatible with Python 3.6)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/)

# Virtualenv

Start your virtual env:

## First time

```bash
virtualenv --python=python3 -q .venv
```

## Activating

```bash
. .venv/bin/activate
```

# Makefile

Or _WTF do I do with that f%$#ing Makefile?_ section.
Well, a `Makefile` makes your life a bit easier, see below.

## Simple build
```bash
make
```

## Tests
```bash
make test
```
