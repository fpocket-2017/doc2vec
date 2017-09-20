# coding: utf-8
import codecs
import os
import re
import pickle

from gensim.models.doc2vec import LabeledSentence

PATH_GPATENT = u'data/gpatent/splitted'
PATH_OUTPUT  = u'data/input'

# Make a list of files in the specified directory
flist = os.listdir(PATH_GPATENT)

# docs list
docs = [] 

# Loop in flist
for idx, file in enumerate(flist):
    print('{}: {}'.format(idx, file))
    
    fp_in = codecs.open('{}/{}'.format(PATH_GPATENT, file), 'r', 'utf-8')

    # Split documents into words
    words = re.split(u' ', fp_in.read())

    # Make a labeled sentence
    try:
        doc = LabeledSentence(
                words = words,
                tags  = [file]
              )
    except:
        print('Can not convert into labeled sentence')
        continue

    docs.append(doc)

with codecs.open('{}/{}'.format(PATH_OUTPUT, 'docs.bin'), 'wb') as fp_out:
    pickle.dump(docs, fp_out)

