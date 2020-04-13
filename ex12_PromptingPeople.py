# Exercise 12: Prompting People

age = input("How old are you? ")
height = input("how tall are you? ")
weight = input("how much do you weight? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy. ")


"""About pydoc
Generate Python documentation in HTML or text for interactive use.

At the Python interactive prompt, calling help(thing) on a Python ojbect
documents the object, and calling help() starts up an interactive
help session.

Or, at the shell command line outside of Python:

Run "python3 -m pydoc <name>" to show documentation on something. <name> may be
the name of function, module, package, or a dotted reference to a
class or function within a module or module in a package. If the 
argument contains a path segment delimiter (e.g. slash on Unix,
backslash on Windows) it is treated as the path to a Python source file.

Run "pydoc -k <keyword>" to search for a keyword in the synopsis lines
of all available modules.

Run "pydoc -n <hostname> to start an HTTP server with the given
hostname (default: localhost) on the local machine.

Run "pydoc -p <port>" to start an HTTP server on the given port on the
local machine. Port number 0 can be used to get an arbitrary unused port.

Run "pydoc -b" to start an HTTP server on an arbitrary unused port and
open a Web browser to interactively browse documentation. Combine with
the -n and -p options to control the hostname and port used.

Run "pydoc -w <name>" to write out the HTML documentation for a module
to a file named "<name>.html".
"""
