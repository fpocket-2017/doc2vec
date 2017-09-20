# coding: utf-8

import const

from owakati import owakati
from docs    import docs
from extract import extract

# Extract "Background of the invention" from "Description
extract(
    const.PATH_INPUT,
    const.PATH_OUTPUT_IM1
    )

" Split contents of "Background of the invention"
owakati(
    const.PATH_OUTPUT_IM1,
    const.PATH_OUTPUT_IM2
    )

# Make "Labeled sentence"
docs(
    const.PATH_OUTPUT_IM2,
    const.PATH_OUTPUT
    )
