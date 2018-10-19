# EDA

1. [Check and Validate Data](00_check_validate.ipynb)
	- If any issues are found, adjust [clean_json.py](../01_data_collection/02_clean_json.py) to make sure no values are incorrect or missing.
2. [Compare Categories](01_eda_books.ipynb)
	- Visually compare differences such as authorship, generations, and book length.

# Data Dictionary

|     key     | type |                                                     description                                                    |
|:-----------:|:----:|:------------------------------------------------------------------------------------------------------------------:|
| category_id |  int | Unique id for each category on Shamela. For the four schools in questions, the ids are '134', '135', '136', '137'. |
|   book_id   |  int |              Unique id for each book. IDs are unique throughout all books, not just within categories.             |
|  author_id  |  int |                                             Unique id for each author.                                             |
| author_name |  str |                                                   Name of author.                                                  |
|  author_dd  |  int |              Year author passed away. This is recorded in Islamic Lunar Years. Add 578 to get CE year.             |
|    pages    |  int |                                      Number of pages the book has on Shamela.                                      |
|  num_words  |  int |                                            Number of words in each book.                                           |
|     text    |  str |              Entire book represented as a string object. To be tokenized into a list of strings later.             |