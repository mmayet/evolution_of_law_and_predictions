import io
import re
import time
import json
import requests
from bs4 import BeautifulSoup

book_titles = {}

with open('../../data/all_books_per_category_saved.json') as f:
    data = json.load(f)

def get_id(index_url):
    return re.findall(r'(\d+)',str(index_url))[0]

def get_soup(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    return BeautifulSoup(response.text, "lxml")

def get_book_text(index_url):
    book_id = get_id(index_url)
    soup = get_soup('http://shamela.ws/index.php/book/'+get_id(book_id))
    title = soup.find('h3', {'class': 'contentTitle-h3'}).text
    book_titles[book_id] = title
    print('ID: {} - Title {}'.format(book_id,title), end="\r")

def save_book_titles():
    for category_index in [27,29,30,32]:
        category_url = list(data.keys())[category_index]
        print('##########\nCategory {}\n##########'.format(category_index))
        for title,index_url in data[list(data.keys())[category_index]]:
            get_book_text(index_url)

    with open('../../data/book_titles.json', 'w') as fp:
            json.dump(book_titles, fp)

# enumerated list of:
# 1. Index of book in folder (and thus how it's read with `glob`)
# 2. `book_id` as a reference
# 3. `book_title` in Arabic
def save_book_order():
    for category_id in ['134','135','136','137']:
        order_book_dict = {}
        for i,file_name in enumerate(glob('../../data/'+str(category_id)+'/*.json')):
            with open(str(file_name)) as f:
                book = json.load(f)
                
            book['title'] = book_titles[str(book['book_id'])][0]
            order_book_dict[i] = [book['title'], book['book_id']]
            print(i, [book['book_id'], book['title']])
            
        with open('../../data/'+str(category_id)+'_book_order.json', 'w') as fp:
            json.dump(order_book_dict, fp)

save_book_titles()
save_book_order()