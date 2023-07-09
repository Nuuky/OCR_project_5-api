from api.nlp.predict import get_topics_from_html, get_topics_from_text


def test_get_topics_from_html():
    html = "<p>consider the <code>pd.Series</code> <code>s</code></p> <pre><code>import pandas as pd import</code></pre><p>"
    res = get_topics_from_html(html)
    assert res == ['file', 'data', 'image', 'application', 'app']
