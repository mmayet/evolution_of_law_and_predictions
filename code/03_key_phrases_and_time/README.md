## Processing The Data to be Modeled
#### [`00_create_texts_dicts_corpora.py`](00_create_texts_dicts_corpora.py)
This is where the book, represented as a giant string is processed.
1. Each `text` key from the `book.json` is loaded.
2. The entire corpus is stripped of Arabic vowels and excess strings.
3.  The magic of [`PyArabic`](https://github.com/linuxscout/pyarabic) comes to life. After it strips vowels and stylistic elongations, it will tokenize the document.
4. While doing that, the script checks for stop words, and weird words (that probably are typos).
5. The number of words are counted and saved.
6. The entire category is saved as a `json` of tokenized lists for each book.
7. These tokenized lists are then used to create a [`Gensim Dictionary`](https://radimrehurek.com/gensim/corpora/dictionary.html) which maps words with integer ids.
8. That dictionary is then turned into a BOW (bag of words) which serves as a corpus — a collection of all words within the dictionary.
9. From there, the result of #6 is taken to [`02_tfidf_corpora.ipynb`](02_tfidf_corpora.ipynb)

#### [`01_dtm_models.py`](01_dtm_models.py)
This is where the dynamic topic models are created.
1. The time slices need to be created. (See Below)
2. LDA [`Latent Dirichlet Allocation`](https://radimrehurek.com/gensim/models/ldamodel.html) on each time slice. This is done using [`LdaSeqModel`](https://radimrehurek.com/gensim/models/ldaseqmodel.html). Because of the time slices, it's calls `Dynamic Topic Modeling` to see the *how* topics change over time.

**Note:** Due to my corpus being law texts covering a number of subjects within all categories in eras, both of these methods were not suitable. This is because the topics themselves *do not change*, but rather the method which they are discussed, analyzed, and changed is where the evolution comes from. With that in mind, I had to find another way to see how key words and phrases changed over time. As a result, my failed tests, methods, and approach to evaluating these models can be found [`05_zz_failed_lda.ipynb`](05_zz_failed_lda.ipynb). Thus, I decided to `TFIDF` my corpus based on time to achieve that result, as seen [`02_tfidf_corpora.ipynb`](02_tfidf_corpora.ipynb). 

## 3. Model The Data: [03_key_phrases_and_time](03_key_phrases_and_time) & [04_recommendations](04_recommendations)
The data are modeled in the following way:
Attempt to answer **Questions 1 & 2:**
1. `Dynamic Topic Modeling` — [`01_dtm_models.py`](01_dtm_models.py)
2. `TFIDF` — [`02_tfidf_corpora.ipynb`](02_tfidf_corpora.ipynb)

## 4. Evaluating The Model: [03_key_phrases_and_time](03_key_phrases_and_time) & [04_recommendations](04_recommendations)
The models are evaluated in the following way:
1. `Failed DTM` — [`05_zz_failed_lda.ipynb`](05_zz_failed_lda.ipynb)
2. **Question 1** [`03_words_by_school.ipynb`](03_words_by_school.ipynb)
3. **Question 2** [`04_words_by_school_over_time.ipynb`](04_words_by_school_over_time.ipynb)

## 5. Answering The Questions
***The answer to each of the questions can be found within the notebooks specified above.***

*Note:*
- [`05_zz_failed_lda.ipynb`](05_zz_failed_lda.ipynb) is a skeleton of DTM's evaluation process.
- [`06_zz_basic_count_vectorizer.ipynb`](06_zz_basic_count_vectorizer.ipynb) is simply a basic text > count > json file.