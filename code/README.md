# Indexing [Shamela.ws](http://shamela.ws)

### The point here is to understand the sitemap, and be able to use that to iterate through all of the categories/genres, and thus use that to iterate through every book within a given category.

#### Technicalities:
1. Scraping is terribly slow within a `.ipynb` file.
2. Neither the categories, nor the books, are ordered in a standard manner. Thus, the category and book ids need to be scraped, and can't simply be pulled from a `range(0,10000)` loop of some sort.
3. Within a category, it's possible to have hundreds of books, which leads to the category of books consisting of multiple pages, which also need to be iterated over, within a category.
4. **The most cumbersome** of these is that the books are saved as HTML page by page. There is no single source to get the text of an entire book. So instead of going to the book-page (i.e., `http://shamela.ws/index.php/book/00000`), the corpus of the book must be taken page by page (i.e., `http://shamela.ws/browse.php/book-00000#page-10000`). Thus, this task will take much longer and will be addressed