Python style is governed by a set of documents which are called Python Enhancement Proposals (PEP) - some don't make it past proposal page. 
PEP is a guide - not a mandate.

## Package & module names

*Modules* should have short, all-lowercase names, underscores can be used if it increases readability. *Packages* should be the same, but underscores in the name is discouraged.

Any python file (.py) is a _module_.

Adding a bunch of _modules_ in a directory as well as an `__init__.py` file makes a _package_.
`__init__.py` can be empty, but there is cool stuff that can be done with it. More later..

If `__init__.py` is forgotten in the package. There will be something worse than a failure - exluding `__init__.py` makes it an _implicit namepspace package_. 

## Importing

The import statement in python is as follows:

`import x`

When we import a module we are actually running it, any import statements inside of that module are also run. This does not mean that the sub-modules imports are available to the calling module, but all of the imports in the file tree have to exist. Otherwise there would be an error:

`ModuleNotFoundError`

### Do's & Don'ts

There are actually a number of ways of importing, but most of them should rarely, if ever be used.