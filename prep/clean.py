# -*- coding: utf-8 -*-

import codecs
import os
import re

def clean(
    path_input,
    path_output
    ):

    # Make a list of files in the specified directory
    flist = os.listdir(path_input)

    # Loop in flist
    total_count = len(flist)
    for idx, file in enumerate(flist):
        print('Clean {0}/{1}: {2}'.format(idx + 1, total_count, file))

        # Skip special file
        if re.match(u'\.', file) != None:
            print('Skipped because hidden file')
            continue

        # Open a file in the list
        with codecs.open('{0}/{1}'.format(path_input, file), 'r', 'utf-8') as fp_in:
            m = re.sub(u'\n| ', u'', fp_in.read())
            
            with codecs.open('{0}/{1}'.format(path_output, file), 'w', 'utf-8') as fp_out:
                fp_out.write(m)