# coding: utf-8

import codecs
import pickle

from gensim import models

PATH_INPUT  = u'data/input'
PATH_OUTPUT = u'data/output'

EPOCHS = 20

with codecs.open('{}/{}'.format(PATH_INPUT, u'docs.bin'), 'rb') as fp_in:
     docs = pickle.load(fp_in)

# Make a model
print('Making model...')
model = models.Doc2Vec(
            docs,
            dm        = 0,
            size      = 617,
            window    = 15,
            alpha     = .025,
            min_alpha = .025,
            min_count = 1,
            sample    = 1e-6
        )

# Train the model
for epoch in range(EPOCHS):
    print('Epoch: {}'.format(epoch + 1))
    
    model.train(
        docs,
        total_examples = 617,
        epochs = EPOCHS
    )
    
    model.alpha -= (0.025 - 0.0001) / 19
    model.min_alpha = model.alpha

# Save the model
model.save('{}/{}'.format(PATH_OUTPUT, 'doc2vec.model'))