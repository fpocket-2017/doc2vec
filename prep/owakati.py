# coding: utf-8
import codecs
import os

import MeCab

PATH_INPUT  = u'data/gpatent/original'
PATH_OUTPUT = u'data/gpatent/splitted'

tagger = MeCab.Tagger(u'-Owakati')

# Make a list of files in the specified directory
flist = os.listdir(PATH_INPUT)

# Loop in flist
for file in flist:
    print('file: {}'.format(file))

    # Open a file in the list
    fp_in = codecs.open('{}/{}'.format(PATH_INPUT, file), 'r', 'utf-8')

    # Split content of the file into words and save it
    fp_out = codecs.open('{}/{}'.format(PATH_OUTPUT, file), 'w', 'utf-8')
    
    try:
        fp_out.write(tagger.parse(fp_in.read()))
    except:
        pass

    fp_out.close()