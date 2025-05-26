Packages are namespaces containing multiple packages and modules. They're just directories, but with certain requirements.

Each package in Python is a directory which MUST contain a special file called __init__.py. This file, which can be empty, indicates that the directory it's in is a Python package. That way it can be imported the same way as a module.