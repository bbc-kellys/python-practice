Python style is governed by a set of documents which are called Python Enhancement Proposals (PEP) - some don't make it past proposal page. 
PEP is a guide - not a mandate.

## Package & module names
____
*Modules* should have short, all-lowercase names, underscores can be used if it increases readability. *Packages* should be the same, but underscores in the name is discouraged.

Any python file (.py) is a _module_.

Adding a bunch of _modules_ in a directory as well as an `__init__.py` file makes a _package_.
`__init__.py` can be empty, but there is cool stuff that can be done with it. More later..

If `__init__.py` is forgotten in the package. There will be something worse than a failure - exluding `__init__.py` makes it an _implicit namepspace package_. 

## Importing
____
The import statement in python is as follows:

`import x`

When we import a module we are actually running it, any import statements inside of that module are also run. This does not mean that the sub-modules imports are available to the calling module, but all of the imports in the file tree have to exist. Otherwise there would be an error:

`ModuleNotFoundError`

### Do's & Don'ts
____
There are actually a number of ways of importing, but most of them should rarely, if ever be used.
Imagine we have a file `smart_door.py`

```
def close():
    print("Ahhhhhhhh.")

def open():
    print("Thank you for making a simple door very happy.")
```

If we want to run the function _open_, from the Python interactive shell, we have to first import the module smart_door
`smart_door` is the _namespace_ of open().

At a certain point though, namespaces can become a pain - or ridiculous

`foo.bar.baz.whatever.doThing()` for example. There is a way around this however.

If we want to be able to use the open function in another file or in the Python interactive shell.

```
from smart_door import open

open()
```

There is flexibility in the import statement, the import can go as far down the module/package path as we need.
However there comes a point where we will want to import almost all of the functions in a namespace.

we _could_ use something like

```
from smart_door import *
```

However, this is very very bad. It can result in _shadowing_ (redfining) of functions for example

```
from smart_door import *
from gzip import *
```

the `smart_door open()` function then becomes _shadowed_ & useless, the `gzip open()` function will be the one called, this is due to it being the last imported & therefore the last defined.

The _Zen of Python_ addresses these sceanrios - **Explicit is better than implicit**

Never guess where a function or variable is coming from, there shoudl always be somewhere in the code that tells us explicitly where something is coming from.

`foo.bar.baz.whatever.doThing()` - is also frowned upon. the advice here is that **flat is better than nested**.

## Importing within Project
____
```
omission-git
├── LICENSE.md
├── omission
│   ├── app.py
│   ├── common
│   │   ├── classproperty.py
│   │   ├── constants.py
│   │   ├── game_enums.py
│   │   └── __init__.py
│   ├── data
│   │   ├── data_loader.py
│   │   ├── game_round_settings.py
│   │   ├── __init__.py
│   │   ├── scoreboard.py
│   │   └── settings.py
│   ├── game
│   │   ├── content_loader.py
│   │   ├── game_item.py
│   │   ├── game_round.py
│   │   ├── __init__.py
│   │   └── timer.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── resources
│   └── tests
│       ├── __init__.py
│       ├── test_game_item.py
│       ├── test_game_round_settings.py
│       ├── test_scoreboard.py
│       ├── test_settings.py
│       ├── test_test.py
│       └── test_timer.py
├── pylintrc
├── README.md
└── .gitignore
```
in `game_round_settings.py`, we want to use my GameMode class. This is defined in `omission/common/game_enums.py`

To achieve this, we use an `absolute import` like this:

```
from omission.common.game_enums import GameMode
```

packages on one level have no knowledge of their siblings. However they do know about their parents, this allows us to do `relative` imports.

`..` means this package's direct parent package.

Use absolute imports whenever possible - it makes the code a lot more readable. Remember - explicit is better than implicit.


## Gotcha
___

In `omission/data/settings.py` we have the line

```
from omission.data.game_round_settings import GameRoundSettings
```

Since both modules are in the `/data/` directory, surely we use `from game_round_settings`

No: we have to call as

```
from .game_round_settings import GameRoundSettings
```

A Single `.` means this package.

## Main
___

the `__main__.py` file in the top level of the package is used to run the whole application from the root of the repo, with the command

```
python -m omission
```

the contents of the `__main__.py` file are as follows:

```
from omission import app

if __name__ = '__main__':
    app.run()
```

`__name__` is a special string attribute of every Python module. if we were to stick the line `print(__name__)` at the top of a py file. Whent the module got imported & thus run, we'd see `path.to.file.py` printed out.

So the check for `__main__` is to check for the **main module** 