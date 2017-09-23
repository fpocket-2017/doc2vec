# -*- coding: utf-8 -*-

import os
import codecs
import re
import shutil
import pdb

from const  import *
from gensim import models

# Load model file
print('Loading model file ...')
model = models.Doc2Vec.load('{0}/{1}'.format(PATH_INPUT, u'model.bin'))

 # Make an inference
print('Makind an inference ...')
if os.path.exists(PATH_INPUT_DOCS):
    files = os.listdir(PATH_INPUT_DOCS)

    total_count = len(files)
    for idx, file in enumerate(files):
        print('{0}/{1}: {2}'.format(idx + 1, total_count, file))
        results = model.docvecs.most_similar(
                    file,
                    topn = 5
                    )

        name      = re.match('(.*)\.txt', file).group(0)
        path_dir  = '{0}/{1}'.format(PATH_OUTPUT, name)
        os.mkdir(path_dir)
        
        with codecs.open('{}/{}'.format(path_dir, u'result.txt'), 'w') as fp_out:
            fp_out.write('{0}:\n'.format(name))
            
            for idx, result in enumerate(results):
                fp_out.write(u'{0}: {1}\n'.format(idx, result))
                shutil.copy2(
                        '{0}/{1}'.format(PATH_INPUT_DOCS, file),
                        '{0}/0_{1}'.format(path_dir, file)
                        )
                    
                if os.path.exists('{0}/{1}'.format(PATH_INPUT_DOCS, result[0])):
                    shutil.copy2(
                        '{0}/{1}'.format(PATH_INPUT_DOCS, result[0]),
                        '{0}/{1}_{2}'.format(path_dir, idx + 1, result[0])
                    )

else:
    print('Docs dir not exist')