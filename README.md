# Credits

First and foremost, this is a tentative to _pythonize_ the code in [dbatalov/reinforcement-learning](https://github.com/dbatalov/reinforcement-learning).

# Requirements

You need to have the following:
* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [pip](https://pypi.org/project/pip/) (obviously compatible with Python 3.6)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/)

## (Optional) Add the git `pre-commit` hook

The hook is basically to require that all tests pass before accepting your commit.

```bash
cp git_hooks_pre-commit .git/hooks/pre-commit
```

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

## Documentation
```bash
make doc
```

## Debugging Test

You can use you preferred tool, I like [pudb](https://pypi.org/project/pudb/) with [pytest-pudb](https://pypi.org/project/pytest-pudb/).
To invoke `pudb` for your test:

```bash
PYTHONPATH="." py.test --pudb tests/<test file>
```

Example:

```bash
PYTHONPATH="." py.test --pudb tests/test_dict_qtable.py
```

## Notes

The `Makefile` is `virtualenv`ed, this means that it will always use `virtualenv`.

To the nitty-gritty:
* Check if there is already a virtualenv, at `.venv` and, if not, create it.
* Activate the virtualenv
* Execute whatever you want, like build or test
