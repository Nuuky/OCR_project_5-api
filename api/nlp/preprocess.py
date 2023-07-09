from bs4 import BeautifulSoup
import nltk
from nltk import sent_tokenize, word_tokenize
from string import punctuation
import re
import pandas as pd
import pickle

nltk.download('punkt')
nltk.download('stopwords')

tfidf_vectorizer = pickle.load(open("api/nlp/models/tfidf_vectorizer.pkl", "rb"))

errors = [
    [["dont", "dnt"], "don't"],
    [["ive", "iv"], "i've"],
    [["im", "iam"], "i'm"],
]

ponc   = [
    [["s"], "is"],
    [["re"], "are"],
    [["ve"], "have"],
    [["ll"], "will"],
    [["t"], "not"],
    [["m"], "am"]
]


def replace_errors(sent):
    for error in errors:
        sent = re.sub(fr"\b({'|'.join(error[0])})\b", error[1], sent)
    return sent

def preprocess_text(text):
    text = text.casefold()
    
    for p in ponc:
        text = re.sub(f"'({'|'.join(p[0])})", " "+p[1], text)
    
    # on supprime les caractère spéciaux
    text = re.sub(f"[{re.escape(punctuation.replace('-', ''))}]", " ", text)
    # on supprime les possibles "-" en trop
    text = re.sub(r"(\s|\W)?(-+)(\s|$)", " ", text)
    # on supprime les chiffres (inutile pour les tags)
    text = re.sub(r"\b[0-9]+\b\s*", "", text)
    text = re.sub(r'(.)\1{3,}',r'\1', text)
    
    text = " ".join(text.split())
    return text

def tokenize(doc: str):
    sent_tokens = sent_tokenize(doc)
    sent_tokens = [preprocess_text(sent) for sent in sent_tokens]
    sent_tokens = [replace_errors(sent) for sent in sent_tokens]
    sent_tokens = [word for sent in sent_tokens for word in word_tokenize(sent) if word not in punctuation] 
    sparse_matrix = tfidf_vectorizer.transform([" ".join(sent_tokens)])
    return pd.DataFrame(sparse_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

def html_to_text(html):
    soup = BeautifulSoup(html, "html.parser")
    for code in soup.find_all("code"):
        code.decompose()
    return soup.get_text(separator=" ")
