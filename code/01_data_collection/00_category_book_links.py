import re
import json
import requests
from bs4 import BeautifulSoup

site_data = {}

class categories():
    def __init__(self, categories):
        self.categories = categories

def get_soup(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "lxml")

def get_categories():
    categories = []
    
    url = 'http://www.shamela.ws/index.php/categories'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    for category in soup.find_all('li', {'class':'regular-cat'}):
        cat_name = str(category.find('a').text)
        cat_link = str(category.find('a').attrs['href'])
        if re.match('/index\.php/category/\d+',cat_link):
            categories.append((cat_name, cat_link))
    
    with open('../../data/categories.json', 'w') as fp:
        json.dump(categories, fp)
    
    return categories

def get_last_category_page(soup):
    try: 
        last_page = soup.find_all('a', {'href': re.compile(r'/index\.php/category/\d+/page-\d+')})[1]
        return re.findall(r'/index\.php/category/\d+/page-(\d+)',str(last_page))[0]
    except:
        return '1'

def get_books():
    categories = get_categories()
    
    for category in categories[:-1]:
        soup = get_soup('http://www.shamela.ws'+category[1])
        last_page = get_last_category_page(soup)
        
        books = []
        
        for page in range(1,int(last_page)+1):
            soup = get_soup('http://www.shamela.ws'+category[1]+'/page-'+str(page))
            
            print('Category: ', category[0], ' ', category[1],'Page No. ',page)
            for book in soup.find_all('td', {'class':'regular-book'}):
                try:
                    book_name = str(book.find('a').text)
                    book_link = str(book.find('a').attrs['href'])
                    if re.match('/index\.php/book/\d+',book_link):
                        books.append((book_name,book_link))
                except:
                    print('Except: ', book)
        
        site_data[str(category[1])] = books
        
    with open('../../data/all_books_per_category_saved.json', 'w') as fp:
        json.dump(site_data, fp)