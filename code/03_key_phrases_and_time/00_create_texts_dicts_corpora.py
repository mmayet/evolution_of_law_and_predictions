import io
import re
import time
import json
import pickle
from glob import glob

from gensim import corpora
from pyarabic import araby
from nltk.corpus import stopwords
from stop_words import get_stop_words
from nltk.stem.isri import ISRIStemmer

categories = ['134','135','136','137']

# get all stop words & individual letters & common words
sw1 = get_stop_words('arabic') + stopwords.words("arabic")
sw2 = ['ا','أ','إ','ذ','ض','ص','ث','ق','ف','غ','ع','ه','خ','ح','ج','ش','س','ي','ب','ل','ا','ال','ت','ن','م','ك','ئ','ء','ؤ','ر','لا','ى','ة','و','ز','ظ']
sw3 = ["آله", "أبو", "أبي", "أثنى", "أحدهما", "أظهرهما", "أن", "أنه", "أو", "أى", "إلا", "إلخ", "إله", "إلى", "ابن", "ابو","ابي", "الآتي", "الأستاذ", "الأولباب", "الامام", "البصير", "الثانية", "الجلال", "الحمد", "الخ", "الدكتور", "الرحمن", "الرحيم", "الرسول", "السميع","الشارح", "الشيء", "الشيخ", "الصمد", "العبد", "العلامة", "العلي", "الفقير", "القدير", "الكتاب", "الله", "المؤلف", "المؤلفة", "المجلد","المسألة", "المصنف", "النبي", "الي", "انتهى", "انظر", "اهـ", "باب", "بالواو", "بدلالة", "برقم", "بسم", "بعد", "بقيد", "بمثابة", "بن", "به","بها", "بين", "بينهما", "تأمل", "تخريجه", "تعالى", "تعبيره", "ثم", "ثناء", "حتى", "حكاهما", "حمدا", "خصما", "دليلنا", "ذكرنا", "ذكرناه", "ر"]
sw4 = ['فقط','ولعل','اختلافهم','فقولان','فصلوأما','اليه','قدمنا','ثالثها','معنى','تقدم','والله','أنها','بلا','وأن','بفاس','منهم','أعلم','ففيه','وهل','أنها','وأن','ذكره','كلامه','قاله','نقله','منهما','بأنه','بنحو','ومحل','نقل','وجهين','فعلى','كون','وأن','أحد','بلا','','','','','','لقول','أنها','أخذ','ففي','ذكره','فاذا','ويدل','قيل','قالوا','القول','وجه','المعنى','وجهين','باعتبار','اعتبار','بينا','بأس','فلذلك','فلهذا','وقاله','تأويلان','القولين','بقوله','إليه','بذلك','شيئا','عنده','وذاك','لعدم','ومنهم','قولين','عبارة','زيادتي','وينبغي','ولهذا','أكان','وخبر','وحينئذ','رحمهم','فهنا','إليه','فلم','غيره','أيضا','ولسنا','جميعهم','وليسوا','الأوجه','التالية','وثالثها','قلت','وكذلك','وسلم','وقال','شيء','لأن','لأن','فهو','فقال','لأنه','رحمه','فلما','يكن','وابن','رسول','النبي','وقيل','وكذا','وإلا','ونحوه','واحد','فلو','الأول','بأن','والثاني','وجهان','قلنا','الله',"فقال","وعن","ربه", "رحمة", "رسول", "رضى", "رضي", "رقم", "رها", "سبحانه", "سنن", "سيأتي", "شرح", "شيخ", "صلى", "طبقات", "عبد", "على", "عليكم", "عليه", "عن","عند", "عنه", "غير", "فأشبه", "فأما", "فإن", "فإنا", "فإنه", "فائدة", "فافهم", "فالأصح", "فالقاضي", "فالوجه", "فان", "فانه", "فجاز", "فدل", "فصل","فكان", "فلأن", "فلأنه", "فلا", "فلما", "فليتأمل", "فمنهم", "فنقول", "فهذا", "فهل", "فوجهان", "فى", "في", "فيه", "فيها", "قال", "قبل", "قدمناه","قلنا", "قول", "قولان", "قوله", "كان", "كتاب", "كلام", "كلامهم", "كما", "كونه", "لأنا", "لأنه", "لأنها", "لان", "لانه", "لخبر", "لذلك", "لرحمة","لقوله", "له", "لهم", "لو", "مادة", "مثال", "مثلا", "عبدا", "مع", "معطوف", "مقدمة", "من", "مناهج", "منتهى", "منه", "نسخة", "نسلم", "نصا","نصه", "نقول", "هريرة", "ههنا", "وأصحهما", "وأما", "وأيضا", "وإن", "وإنما", "وإنه", "واحتج", "واعلم", "والتقوى", "والثانى", "والثاني","والسلام", "والصلاة", "وان", "وانظر", "وبالله", "وبه", "وتقدم", "وجزم", "وجل", "وجهان", "وسلم", "وسن", "وشرعا", "وصلى", "وعبارة", "وعلى","وعنه", "وغيره", "وغيرهم", "وفى", "وقال", "وقد", "وقدمه", "وقوله", "وقولي", "وقيل", "وكذلك", "ولأن", "ولأنه", "ولأنها", "ولذا", "ولكنا", "ولنا", "ولو","عنهم", "وهذا", "وهنا",'فذا','فهذ','هتحقيق','فاستخلفه','واعتبارا','وبالجملة','اليها','وذا',"وهو", "ويحتمل", "يعني", "يقال", "يقول", "يكون"]
sw = set(sw1+sw2+sw3+sw4)

st = ISRIStemmer()			# NLTK Stemmer

def not_sw(text):			# excludes stop words
    return (text not in sw) or st.stem(text) not in sw

def not_small_big(text):	# exclude single letters, combined words, and stop words
    return (len(text) >= 3) and (len(text) <= 9)

def get_book_id(index_url):	# returns book_id
    return re.findall(r'13\d\\(\d+)',str(index_url))[0]

def strip_text(text):		# removes arabic vowels and stylistic spacing
    return araby.strip_tatweel(araby.strip_tashkeel(text))

# Each book is processed and tokenized
# Each tokenized book is a list of words
# Each list is then a tokenized book
# `texts` is a list each tokenized book
# It's fine that `texts` is currently a list and not a dict
# because it will be open and read as a JSON
def create_texts(category_id,order):
	texts = []

	for i,file_name in enumerate([i[1] for i in order]):
		with open(str('../../data/'+str(category_id)+'/'+str(file_name)+'.json')) as f:
			book = json.load(f)
			
		start = time.time()
		print('Category: {} - #{} - Book: {}'.format(category_id,i, str(file_name)), end="\r")
		texts.append(araby.tokenize(strip_text(book['text']), conditions=[not_sw,araby.is_arabicword,not_small_big]))
		print("Category: {} - #{} - Book: {} took {} seconds to clean and tokenize.\n".format(category_id,i, str(file_name),time.time()-start), end="\r")
		
		add num_words to book.json
		book['num_words'] = len(texts[i])
		with io.open('../../data/'+str(category_id)+'/'+str(book['book_id'])+'.json','w',encoding='utf8') as f:
			json.dump(book, f)

	# save texts
	with io.open('gensim_files/texts_'+str(category_id)+'.json','w',encoding='utf8') as f:
		json.dump(texts, f)
	
	print('Finished `create_texts()` for Category: {}.'.format(category_id))
	return texts

# Creates a Gensim Dictionary
# Give each word in the book an id
def create_dict(category_id,texts):
	# turn tokenized documents into a id <-> term dictionary
	# then filter out extremes
	dictionary = corpora.Dictionary(texts)
	dictionary.filter_extremes(no_below=15, no_above=0.7)
	dictionary.filter_n_most_frequent(10)
	dictionary.save_as_text("gensim_files/dict_"+str(category_id)+".dict")
	
	print('Finished `create_dict()` for Category: {}.'.format(category_id))
	return dictionary

# Creates a Bag of Words
# Which is a matrix of words for each book
def create_corpus(category_id,texts,dictionary):
	# convert tokenized documents into a document-term matrix
	corpus = [dictionary.doc2bow(text) for text in texts]
	corpora.MmCorpus.serialize('gensim_files/corpus_'+str(category_id)+'.mm', corpus)

	print('Finished `create_corpus()` for Category: {}.'.format(category_id))
	return corpus

# create list of tuples
# that order book_id by author_dd
# so that LdaSeqModel can read books chronologically
# use this to open .json dict w/ proper order:
# https://stackoverflow.com/questions/43789439/python-json-loads-changes-the-order-of-the-object  
def order_books_by_year():
    for category_id in categories:
        book_order = []
        for file_name in glob('../../data/'+str(category_id)+'/*.json'):
            with open(str(file_name)) as f:
                date = json.load(f)['author_dd']
                book_order.append((int(date),get_book_id(file_name)))

        book_order = sorted(book_order, key=lambda x: x[0])
        with io.open('../../data/'+str(category_id)+'_simple_book_order.json','w',encoding='utf8') as f:
            json.dump(book_order, f)

def load_book_order(category_id):
	with open('../../data/'+str(category_id)+'_simple_book_order.json') as f:
		return json.load(f)

for category_id in categories:
	print('\n#####\n#{}#\n#####\n'.format(category_id))
	order = load_book_order(category_id)
	texts = create_texts(category_id,order)
	dictionary = create_dict(category_id,texts)
	corpus = create_corpus(category_id,texts,dictionary)