# Credits

First and foremost, this is a tentative to _pythonize_ the code in [dbatalov/reinforcement-learning](https://github.com/dbatalov/reinforcement-learning).

# Requirements

You need to have the following:
* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [pip](https://pypi.org/project/pip/) (obviously compatible with Python 3.6)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/)

# Virtualenv

If you use the `Makefile` it will always set your environment to use `virtualenv`.
You can always get out of your virtualenv by issuing `deactivate`.

## Activate

This is only necessary if are doing things outside the `Makefile`, like adding a new dependency.

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

## Notes

The `Makefile` is `virtualenv`ed, this means that it will always use `virtualenv`.

To the nitty-gritty:
* Check if there is already a virtualenv, at `.venv` and, if not, create it.
* Activate the virtualenv
* Execute whatever you want, like build or test
