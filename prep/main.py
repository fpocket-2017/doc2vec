# -*- coding: utf-8 -*-

from const   import *
from clean   import clean
from owakati import owakati
from docs    import docs

# Clean contents of files in the specified directory
clean(
    PATH_INPUT,
    PATH_OUTPUT_IM1
    )

# Split contents of "Background of the invention"
owakati(
    PATH_OUTPUT_IM1,
    PATH_OUTPUT_IM2
    )

# Make "Labeled sentence"
docs(
    PATH_OUTPUT_IM2,
    PATH_OUTPUT
    )
