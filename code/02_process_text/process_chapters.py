import json
import re
from glob import glob

from nltk.stem.isri import ISRIStemmer
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

class Books():
    def __iter__(self):
        for i,file_name in enumerate(glob('../../data/134/*.json')):
            try:
                with open(str(file_name)) as f:
                    book_text = json.load(f)['text']
                
                #### Start Processing
                st = ISRIStemmer()
                stemmed_book = st.stem(book_text)
                print(str(file_name))
                yield TaggedDocument(stemmed_book,[i])

            except:
                print("Fix {}".format(file_name))

alpha = .025
min_alpha = .00025
min_count = 1
dm = 1

model_137 = Doc2Vec(documents=Books())
model_137.save("137.model")
print("Model Saved")

# ```
# https://medium.com/scaleabout/a-gentle-introduction-to-doc2vec-db3e8c0cce5e
# https://radimrehurek.com/gensim/models/doc2vec.html
# ```