# coding: utf-8

import codecs
import os

import MeCab

def owakati(
    path_input,
    path_output
    )

    tagger = MeCab.Tagger(u'-Owakati')

    # Make a list of files in the specified directory
    flist = os.listdir(path_input)

    # Loop in flist
    for file in flist:
        print('file: {}'.format(file))

        # Open a file in the list
        with codecs.open('{}/{}'.format(path_input, file), 'r', 'utf-8') as fp_in

            # Split content of the file into words and save it
            with codecs.open('{}/{}'.format(path_output, file), 'w', 'utf-8') as fp_out
    
            try:
                fp_out.write(tagger.parse(fp_in.read()))
            except:
                pass
                