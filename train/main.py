# -*- coding: utf-8 -*-

import codecs
import pickle

from const  import *
from gensim import models

EPOCHS = 20

# Load docs file
print('Loading docs file...')
with codecs.open('{}/{}'.format(PATH_INPUT, u'docs.bin'), 'rb') as fp:
     docs = pickle.load(fp)

# Make a model
print('Making a model...')
model = models.Doc2Vec(
            size      = 10,
            alpha     = 0.0015,
            sample    = 1e-5,
            min_count = 1,
        )

# Train a model
print('Training the model...')
model.build_vocab(docs)

print('corpus_count: {0}'.format(model.corpus_count))
print('epochs      : {0}'.format(model.iter))
model.train(
    docs,
    total_examples = model.corpus_count,
    epochs         = 200
    )

# Save the model
print('Saving the model...')
model.save('{}/{}'.format(PATH_OUTPUT, 'model.bin'))