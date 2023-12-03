import nltk
from nltk.tokenize import RegexpTokenizer

def similaridade(text1, text2):
    f = open(text1, "r", encoding="utf-8")
    texto1 = f.read()
    print(texto1)
    f = open(text2, "r", encoding="utf-8")
    texto2 = f.read()
    print(texto2)
    tokenizer = RegexpTokenizer(r'[A-z]\w*')
    tokens = tokenizer.tokenize(texto)
    stopwords = nltk.corpus.stopwords.words('portuguese')
    listaMinhasSW = ['[',']']
    stopwords.extend(listaMinhasSW)

similaridade("text1.txt", "text2.txt")