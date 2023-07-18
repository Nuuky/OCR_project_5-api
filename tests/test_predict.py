from api.nlp.predict import get_topics_from_html, get_topics_from_text


def test_get_topics_from_has_same_prediction():
    html = "<p>consider the <code>pd.Series</code>  data <code>s</code></p> <pre><code>import pandas as pd import</code></pre><p>"
    res_html = get_topics_from_html(html)
    text = "consider the data"
    res_text = get_topics_from_html(text)

    assert res_html == res_text
    assert len(res_html) == 5
