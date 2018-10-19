import re
import json
import time
from glob import glob

from gensim import corpora
from pyarabic import araby
from nltk.corpus import stopwords
from stop_words import get_stop_words
from nltk.stem.isri import ISRIStemmer
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

categories = ['134','135','136','137']

class Books():

    def __init__(self, category_id):
        self.category_id = category_id
        print('Books Class instantiated for Category {}.'.format(category_id))

        # NLTK Stemmer
        self.st = ISRIStemmer()

        # get all stop words
        # individual letters (typos & printing issues)
        sw1 = get_stop_words('arabic') + stopwords.words("arabic")
        sw2 = ['ا','أ','إ','ذ','ض','ص','ث','ق','ف','غ','ع','ه','خ','ح','ج','ش','س','ي','ب','ل','ا','ال','ت','ن','م','ك','ئ','ء','ؤ','ر','لا','ى','ة','و','ز','ظ']
        self.sw = set(sw1+sw2)

    def not_sw(self, text):			# excludes stop words
        return (text not in self.sw) or self.st.stem(text) not in self.sw

    def not_small_big(self, text):	# exclude single letters, combined words, and stop words
        return (len(text) >= 3) and (len(text) <= 9)

    def get_book_id(self, index_url):
        return re.findall(r'13\d\\(\d+)',str(index_url))[0]

    def strip_text(self, text):
        return araby.strip_tatweel(araby.strip_tashkeel(text))

    # This function is the main reason for having this class
    # Since  Doc2Vec can take a `iter` to go through each file
    # one at a time, instead of loading all the books into memory.
    def __iter__(self):
        for i,file_name in enumerate(glob('../../data/'+str(self.category_id)+'/*.json')):
            print('Started Book: {}.'.format(self.get_book_id(file_name)))
            try:
                with open(str(file_name)) as f:
                    book_text = json.load(f)['text']
                
                #### Start Processing
                start_time = time.time()
                processed_book = araby.tokenize(self.strip_text(book_text),conditions=[self.not_sw,araby.is_arabicword])
                print('Cleaned Book: {} in {} seconds.'.format(self.get_book_id(file_name),time.time()-start_time))
                yield TaggedDocument(processed_book,[i])

            except:
                print("Fix {}".format(file_name))

def create_doc2vec_models():
    for category_id in categories:
        
        print('Starting Doc2Vec on Category {}.'.format(category_id))
        start_time = time.time()
        doc2vec_model = Doc2Vec(documents=Books(category_id))

        doc2vec_model.save('doc2vec_models/doc2vec_'+str(category_id)+'_simple.model')
        print("Model {} Saved. It took {} seconds.".format(category_id,time.time()-start_time))

def create_recommendations():
    d2v_models = {}
    book_orders = {}
    categories = [134,135,136,137]

    for category_id in categories:
        d2v_models[category_id] = Doc2Vec.load('doc2vec_models/doc2vec_'+str(category_id)+'_simple.model')
        with open('../../data/'+str(category_id)+'_book_order.json') as f:
            book_orders[category_id] = json.load(f)

    for category_id in categories:
        category_recommendations = {}
        for x in range(d2v_models[category_id].corpus_count):
            category_recommendations[book_orders[category_id][str(x)][0]] = []
            for i,y in enumerate(d2v_models[category_id].docvecs.most_similar(x)):
                category_recommendations[book_orders[category_id][str(x)][0]].append((book_orders[category_id][str(y[0])][0]))
        with open('../../data/category_'+str(category_id)+'_recomendations.json', 'w') as fp:
                json.dump(category_recommendations, fp)

'''
Originally, Doc2Vec models were tuned and trained, thinking this would be the best way to create the best recommendations.
However, after tuning, testing, and reviewing, it seemed that the simplest model worked best.
There was no adjustment in the learning rate (alpha), no corpus (words of all books), no neural network training.
Just a series of TaggedDocuments (i.e., a book with an id) being turned into vectors.
These are then used to find distances an cosine similarites.
'''

# for category_id in categories:    
#     dm          = 1
#     epochs      = 10
#     str_alpha   = 0.025
#     end_alpha   = 0.00025
#     #corpus      = load_corpus(category_id)
    
#     print('Starting Doc2Vec on Category {}.'.format(category_id))
#     start_time = time.time()
#     doc2vec_model = Doc2Vec(documents=Books(category_id),dm=dm,alpha=str_alpha,min_alpha=end_alpha)
    
#    for epoch in range(epochs):
#        doc2vec_model.train(corpus_file=corpus,total_examples=doc2vec_model.corpus_count)
#        print('Trained Epoch {}.'.format(str(epoch)))

#     doc2vec_model.save('gensim_files/doc2vec_'+str(category_id)+'.model')
#     print("Model {} Saved. It took {} seconds.".format(category_id,time.time()-start_time))