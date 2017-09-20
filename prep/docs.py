# coding: utf-8

import codecs
import os
import re
import pickle

from gensim.models.doc2vec import LabeledSentence

def docs(
    path_input,
    path_output
    )
    
    # Make a list of files in the specified directory
    flist = os.listdir(path_input)

    # docs list
    docs = [] 

    # Loop in flist
    for idx, file in enumerate(flist):
        print('{}: {}'.format(idx, file))
    
        with codecs.open('{}/{}'.format(path_input, file), 'r', 'utf-8') as fp

            # Split documents into words
            words = re.split(u' ', fp.read())

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

    with codecs.open('{}/{}'.format(path_output, 'docs.bin'), 'wb') as fp:
        pickle.dump(docs, fp)

