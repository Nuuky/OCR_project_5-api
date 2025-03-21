import pandas as pd
import pickle

from api.nlp.preprocess import tokenize, html_to_text, tfidf_vectorizer

lda_model = pickle.load(open("api/nlp/models/lda_model.pkl", "rb"))
terms = tfidf_vectorizer.get_feature_names_out()


def get_lda_topic_components(n=5):
    topics = list()
    for _, component in enumerate(lda_model.components_):
        zipped = zip(terms, component)
        top_terms_key=sorted(zipped, key = lambda t: t[1], reverse=True)[:n]
        top_terms_list=list(dict(top_terms_key).keys())
        topics.append(top_terms_list)
    return topics

def get_topics_from_text(text: str) -> list[str]:
    tokens = tokenize(text)
    lda_topics = get_lda_topic_components(n=5)
    pred = lda_model.transform(tokens)
    y_pred_list = [lda_topics[i] for i in pred.argmax(axis=1)]
    return y_pred_list[0]

def get_topics_from_html(html: str) -> list[str]:
    text = html_to_text(html)
    return get_topics_from_text(text)
