# Indexing [Shamela.ws](http://shamela.ws)

## The point here is to understand the site-map, and be able to use that to iterate through all of the categories/genres, and thus use that to iterate through every book within a given category.

## Process:
1. [`00_category_book_links.py`](00_category_book_links.py) Get direct links to every category, and every book within that category. Save that as a `.json` for further traversals.
2. [`01_scrape_books.py`](01_scrape_books.py) Collect every page of every book, along with relevant information (author name, author death date, number of pages), create a `Book` object, and then save each book as a `.json`. (*Note: Once all the data are gathered, all the book files will be dynamically pushed to a PostgreSQL DB in AWS.*)
3. [`02_clean_json.py`](02_clean_json.py) Scan through all the `Book.json` files ensuring that all numbers are properly encoded as `int64` objects, strings are properly encoded as `object`, and verify all the data (as best as a computer can).

#### Technicalities:
1. Scraping is terribly slow within a `.ipynb` file.
2. Neither the categories, nor the books, are ordered in a standard manner. Thus, the category and book ids need to be scraped, and can't simply be pulled from a `range(0,10000)` loop of some sort.
3. Within a category, it's possible to have hundreds of books, which leads to the category of books consisting of multiple pages, which also need to be iterated over, within a category.
4. **The most cumbersome** of these is that the books are saved as HTML page by page. There is no single source to get the text of an entire book. So instead of going to the book-page (i.e., `http://shamela.ws/index.php/book/00000`), the corpus of the book must be taken page by page (i.e., `http://shamela.ws/browse.php/book-00000#page-10000`). Thus, this task will take much longer and will use it's own scraper file.
5. Since the book files can be extremely large, they will not be pushed to GitHub.