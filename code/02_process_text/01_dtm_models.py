import pickle
from gensim import corpora
from gensim.test.utils import datapath
from gensim.models import LdaModel, LdaSeqModel

categories = [134,135,136,137]
time_ranges = {
    134: [7, 6, 10, 10, 10, 5],
    135: [2, 18, 12, 8, 17, 9],
    136: [2, 8, 15, 10, 16, 9],     # [1, 9, 15, 10, 16, 9]   Used time w/ al-Muzanī because of min_df in TFIDF
    137: [6, 10, 12, 12, 20, 17]
}

def load_dict_corpus(category_id):
    dictionary = corpora.Dictionary.load_from_text('gensim_files/dict_'+str(category_id)+'.dict')
    corpus = corpora.MmCorpus('gensim_files/corpus_'+str(category_id)+'.mm')
    
    print('Dictionary & Corpus loaded for Category {}.'.format(category_id))
    return dictionary,corpus

def model_dtm(category_id):
    dictionary,corpus = load_dict_corpus(category_id)
    time_range = time_ranges[category_id]

    ldaseq = LdaSeqModel(corpus=corpus, id2word=dictionary, time_slice=time_range,
                         num_topics=3, chunksize=10, passes=1, random_state=3)
    
    ldaseq.save(datapath('dynamic_topic_models/dtm_'+str(category_id)+'_model'))
    pickle.dump(ldaseq, open('dynamic_topic_models/dtm_'+str(category_id)+'_model.p', 'wb'))
    return ldaseq

for category_id in categories[]:
    print('Starting DTM for Category {}.'.format(category_id))
    model_dtm(category_id)

