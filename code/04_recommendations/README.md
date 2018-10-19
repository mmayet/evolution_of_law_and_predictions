## 3. Model The Data: [`00_create_doc2vec_models.py`](00_create_doc2vec_models.py)
This is where the book, represented as a giant string is processed.
1. Each `text` key from the `book.json` is loaded.
2. The entire corpus is stripped of Arabic vowels and excess strings.
3.  The magic of [`PyArabic`](https://github.com/linuxscout/pyarabic) comes to life. After it strips vowels and stylistic elongations, it will tokenize the document.
4. While doing that, the script checks for stop words, and weird words (that probably are typos).
5. This is all being to to each book one at a time, but loaded into a Python Generator so that [`Doc2Vec`](https://radimrehurek.com/gensim/models/doc2vec.html) can load them one by one without loading everything into memory at once.
6. Doc2Vec then mimics a neural network by feeding batches of these texts and verctorizing the entire texts, and also computing distances between them, along with establishing a vocab, and many other useful features, such as converting individual vectors into Gensim's own [`Word2Vec`](https://radimrehurek.com/gensim/models/word2vec.html).
7. From there, the result of #6 is taken to [`01_review_recommendations.ipynb`](01_review_recommendations.ipynb)

## 4. Evaluating The Model: [`01_review_recommendations.ipynb`](01_review_recommendations.ipynb)
I personally looked at the recommendations. At first, I wasn't so pleased, so I went back and tuned my Doc2Vec parameters. I then tried to hypertune my Doc2Vec (code is at the bottom of [`00_create_doc2vec_models.py`](00_create_doc2vec_models.py)), but that only hurt the results. After tuning the model, I finalized the current model trained in that script.

## 5. Answering The Questions
***The answer to each of the questions can be found within the notebooks specified above.***