import io
import re
import time
import json
import requests
from bs4 import BeautifulSoup

class Categories:
    def __init__(self, categories):
        self.categories = categories

# This class was not used
class Category:
    def __init__(self, link, number_of_books, books):
        self.link = link
        self.number_of_books = set(number_of_books)
        self.books = books

class Books:
    def __init__(self):
        self.books = []

class Book:
    def __init__(self, book_id, author_id, author_name, author_dd, text, pages,category_id):
        self.book_id = book_id
        self.author_id = author_id
        self.author_name = author_name
        self.author_dd = author_dd
        self.text = text
        self.pages = pages
        self.category_id = category_id

# This class was not used
class Author:
    def __init__(self, link, name, books, death_date):
        self.link = link
        self.name = name
        self.books = books
        self.death_date = death_date

with open('../../data/all_books_per_category_saved.json') as f:
    data = json.load(f)

def get_id(index_url):
    return re.findall(r'(\d+)',str(index_url))[0]

def get_soup(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "lxml")

def get_book_text(category_url, index_url):
    book_id = get_id(index_url)
    category_id = get_id(category_url)
    print('Category {} - Book {} - Started'.format(category_id,book_id))
    
    # get book info
    soup = get_soup('http://shamela.ws/index.php/book/'+get_id(book_id))

    author_link = soup.find('a', {'href': re.compile(r'/index\.php/author/\d+')}).attrs['href']
    author_name = soup.find('a', {'href': re.compile(r'/index\.php/author/\d+')}).text
    try:
        author_dd = re.findall(r'المتوفى?[ :][ نحو ]*(\d+)',str(soup))[0]
    except:
        author_dd = -1
    
    # get book text
    soup = get_soup('http://shamela.ws/browse.php/book-'+get_id(index_url))
    
    first_page = int(re.findall(r'var current_page = (\d+);',str(soup))[0])
    last_page = int(re.findall(r'var last_page = (\d+);',str(soup))[0])
    text = ''
    
    for page in range(first_page,last_page+1):
        soup = get_soup('http://shamela.ws/browse.php/book-'+get_id(index_url)+'/page-'+str(page))
        try:
            text += ' ' + str(soup.find('div',{'id':'book-container'}).text)
        except:
            text += ''
        print ("Done with page {} of {}.".format(str(page),str(last_page)), end="\r")
        time.sleep(.01)
                        
    new_book = Book(book_id, get_id(author_link), author_name, author_dd, text, last_page, category_id)
    save_book(new_book)
    all_books.books.append(new_book)
        
    print('Category {} - Book {} - Done'.format(category_id,book_id))

def save_book(new_book):
    book = {}

    book['book_id'] = int(new_book.book_id)
    book['author_id'] = int(new_book.author_id)
    book['author_name'] = new_book.author_name
    book['author_dd'] = int(new_book.author_dd)
    book['text'] = new_book.text
    book['pages'] = int(new_book.pages)
    book['category_id'] = int(new_book.category_id)

    with io.open('../../data/'+str(new_book.category_id)+'/'+str(new_book.book_id)+'.json','w',encoding='utf8') as f:
        json.dump(book, f)

def get_dict_index(cat_url):
    return list(data.keys()).index(cat_url)

# These are the 2 variables needed to run the main loop.
Categories(data.keys())

all_books = Books()

# This is for personal checks to associate category links to category ids.
# get_dict_index('/index.php/category/134') => 27 —— Ḥanafī
# get_dict_index('/index.php/category/135') => 29 —— Mālikī
# get_dict_index('/index.php/category/136') => 30 —— Shāfiʿī
# get_dict_index('/index.php/category/137') => 32 —— Ḥanbalī

'''
This is what calls everything necessary from above. It makes the main call to `get_book_text` which fetches everything.
In reality, this was done with 4 concurrent scripts that each focused on one category to rapidly speed up the process.
'''
for category_index in [27,29,30,32]:
    category_url = list(data.keys())[category_index]

    for title,index_url in data[list(data.keys())[category_index]]:
        print(time.time())
        print(title)
        get_book_text(category_url, index_url)