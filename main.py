import nltk
from nltk.tokenize import RegexpTokenizer
from unidecode import unidecode

def similaridade(text1, text2):
    f = open(text1, "r", encoding="utf-8")
    texto1 = f.read()
    f = open(text2, "r", encoding="utf-8")
    texto2 = f.read()

    texto1 = unidecode(texto1)
    texto2 = unidecode(texto2)

    tokenizer = RegexpTokenizer(r'[A-z]\w*')
    token_text1 = tokenizer.tokenize(texto1)
    token_text2 = tokenizer.tokenize(texto2)

    stopwords = nltk.corpus.stopwords.words('portuguese')
    listaMinhasSW = ['[',']']
    stopwords.extend(listaMinhasSW)

    token01_sem_stopwords = [w for w in token_text1 if w.lower() not in stopwords]
    token02_sem_stopwords = [w for w in token_text2 if w.lower() not in stopwords]

    frequencia_token01 = nltk.FreqDist(token01_sem_stopwords)
    frequencia_token02 = nltk.FreqDist(token02_sem_stopwords)

    palavras_token01 = frequencia_token01.most_common()
    palavras_token02 = frequencia_token02.most_common()

    key_word_token01 = [p[0] for cont, p in enumerate(palavras_token01) if cont < 4]
    key_word_token02 = [p[0] for cont, p in enumerate(palavras_token02) if cont < 4]

    print(key_word_token01)
    print(key_word_token02)
    contador = 0

    for token in key_word_token01:
        print(token)
        for token2 in key_word_token02:
            print(token2)
            if(token == token2):
                contador +=25

    print("A similaridade é de " + str(contador) +  "%")

similaridade("text1.txt", "text2.txt")