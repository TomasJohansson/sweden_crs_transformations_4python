__all__ = [] # nothing in this directory should be considered as "public", and the files and classes also use _ as prefix

# https://stackoverflow.com/questions/36015605/prevent-python-packages-from-re-exporting-imported-names
# the pythonic way to do it is to rely on __all__. It controls not only what is exported on from MODULE import *,
# but also what shows up in help(MODULE), and according to the "We are all adults here" mantra,
# it is the users own fault if he uses anything not documented as public.
# leading underscore, which is a standard Python idiom for communicating "implementation detail, use at your own risk":
