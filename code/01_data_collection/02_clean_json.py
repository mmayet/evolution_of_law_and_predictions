import io
import re
import json
import requests
from glob import glob
from bs4 import BeautifulSoup

class Book:
    def __init__(self, book_id, author_id, author_name, author_dd, text, pages,category_id):
        self.book_id = book_id
        self.author_id = author_id
        self.author_name = author_name
        self.author_dd = author_dd
        self.text = text
        self.pages = pages
        self.category_id = category_id

def get_id(index_url):
    return re.findall(r'(\d+)',str(index_url))[0]

def get_soup(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "lxml")

def save_book(new_book):
    book = {}

    soup = get_soup('http://shamela.ws/index.php/book/'+get_id(new_book.book_id))

    book['book_id'] = int(new_book.book_id)
    book['author_id'] = int(get_id(soup.find('a', {'href': re.compile(r'/index\.php/author/\d+')}).attrs['href']))
    book['author_name'] = new_book.author_name
    book['author_dd'] = int(new_book.author_dd)
    book['text'] = new_book.text
    book['pages'] = int(new_book.pages)
    book['category_id'] = int(new_book.category_id)

    with io.open(str(new_book.category_id)+'/'+str(new_book.book_id)+'.json','w',encoding='utf8') as f:
        json.dump(book, f)

for f_name in glob('../../data/13*/*.json'):
    print(str(f_name))
    try:
        with open(str(f_name)) as f:
            book = json.load(f)

        print(book['category_id'], ' - ', book['book_id'])
        new_book = Book(int(book['book_id']), int(book['author_id']), 
                    book['author_name'], int(book['author_dd']), book['text'], 
                    int(book['pages']), int(book['category_id']))
        save_book(new_book)
    except:
        print("fix: ", str(f_name))