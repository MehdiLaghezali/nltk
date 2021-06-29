import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('treebank')
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag
from nltk.corpus import treebank
import string

f=open("text.txt",'r')
text=f.read()

text=text.lower()
textt=[char for char in text if char not in string.punctuation]
text="".join(textt)

text_words=word_tokenize(text)

stop_words=stopwords.words('english')

filtered_words = [word for word in text_words if word not in stop_words]

porter = PorterStemmer()
stemmed = [porter.stem(word) for word in filtered_words]

pos = pos_tag(filtered_words)



print(text)
print(text_words)
print(stop_words)
print(filtered_words)
print(stemmed)
print(pos)