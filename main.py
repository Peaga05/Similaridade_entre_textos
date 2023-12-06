import nltk
from nltk.tokenize import RegexpTokenizer
from unidecode import unidecode
import requests
from bs4 import BeautifulSoup
import re

def buscarSinonimo(busca):
    listaSinonimos = []
    url = "https://www.lexico.pt/" + busca
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    conts = soup.find_all('div', class_=["card card-pl"])
    tags = soup.find_all('p', class_=["text words-buttons"])

    if (tags.__len__() > 1):
        sinonimos = tags[0].select('span a')
        for palavra in sinonimos:
            listaSinonimos.append(palavra.get_text())
    else:
        if conts and conts[0]:
            titulo_element = conts[0].find('h2', class_=["card-title"])
            if titulo_element:
                titulo = titulo_element.get_text()
                lista = conts[0].select('span a')
                if 'Sinonimo' in titulo or 'Sinónimos' in titulo or 'Sinónimo' in titulo or 'Sinonimos' in titulo:
                    for item in lista:
                        listaSinonimos.append(unidecode(item.get_text()))
    return listaSinonimos

def remover_plural(palavra):
    padrao_plural = re.compile(r'(\w+)(s|es)$', re.IGNORECASE)
    correspondencia = padrao_plural.match(palavra)
    if correspondencia:
        singular = correspondencia.group(1)
        return singular
    else:
        return palavra

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

    key_word_token01 = [remover_plural(palavra) for palavra in key_word_token01]
    key_word_token02 = [remover_plural(palavra) for palavra in key_word_token02]

    print(key_word_token01)
    print(key_word_token02)

    contador = 0
    buscar = True

    for token in key_word_token01:
        buscar = True
        for token2 in key_word_token02:
            if(token.lower() == token2.lower()):
                buscar = False
                contador += 25

        if buscar:
            lista = buscarSinonimo(token)
            for token in lista:
                for token2 in key_word_token02:
                    if(token.lower() == token2.lower()):
                        contador += 12.5


    print("A similaridade é de " + str(contador) +  "%")

similaridade("text1.txt", "text2.txt")
