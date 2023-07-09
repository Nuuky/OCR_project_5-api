from api.nlp.preprocess import replace_errors, preprocess_text, tokenize, html_to_text


def test_replace_errors():
    sent_with_err = "hello iv world dnt im test"
    sent_without_err = "simple sent without error"
    sent1 = replace_errors(sent_with_err)
    sent2 = replace_errors(sent_without_err)
    assert sent1 == "hello i've world don't i'm test"
    assert sent2 == sent_without_err

def test_preprocess_text():
    text = "Hello ! I've been using, python for -- 2 years - 42"
    text1 = preprocess_text(text)
    assert text1 == "hello i have been using python for years"

def test_tokenize():
    doc = "Hello ! I've been using, python for -- 2 years - 42"
    tok = tokenize(doc)
    assert tok == "hello i have been using python for years".split(" ")

def test_html_to_text():
    html = "<html><head><title>Awesome website !</title></head><body><h1>My awesome website</h1><div><p>This is juste an example</p><code>console.log('debug')</code></div></body></html>"
    text = "Hello ! I've been using, python for -- 2 years - 42"
    res1 = html_to_text(html)
    res2 = html_to_text(text)
    assert res1 == "Awesome website ! My awesome website This is juste an example"
    assert res2 == text