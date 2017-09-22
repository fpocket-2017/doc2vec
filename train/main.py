# -*- coding: utf-8 -*-

import codecs
import pickle

from const  import *
from gensim import models

# Load docs file
print('Loading docs file...')
with codecs.open('{}/{}'.format(PATH_INPUT, u'docs.bin'), 'rb') as fp:
     docs = pickle.load(fp)

# Make a model
print('Making a model...')
model = models.Doc2Vec(
            size      = 400,
            alpha     = 0.0015,
            sample    = 1e-5,
            min_count = 1,
        )

# Train a model
print('Training the model...')
model.build_vocab(docs)

model.train(
    docs,
    total_examples = model.corpus_count,
    epochs         = 100
    )

# Save the model
print('Saving the model...')
model.save('{}/{}'.format(PATH_OUTPUT, 'model.bin'))