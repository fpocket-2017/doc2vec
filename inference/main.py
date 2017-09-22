# -*- coding: utf-8 -*-

import codecs

from const  import *
from gensim import models

# Load model file
print('Loading model file ...')
model = models.Doc2Vec.load('{0}/{1}'.format(PATH_INPUT, u'model.bin'))

# Make an inference
print('Making an inference...')
results = model.docvecs.most_similar(
                'JP3161215B2.txt',
                topn = 5
                )
                
# Write result
print('Writing the result...')
with codecs.open('{}/{}'.format(PATH_OUTPUT, u'result.txt'), 'w') as fp_out:
    fp_out.write(u'JP3161215B2.txt:\n')
    for idx, result in enumerate(results):
        fp_out.write(u'{0}: {1}\n'.format(idx, result))
