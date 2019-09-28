from flask import Flask, request, Response, jsonify
from bs4 import BeautifulSoup
from filters_utils import get_filter_value
from functools import reduce

app = Flask(__name__)


@app.route('/')
def default():
    return "You had me at hello"


@app.route('/filter')
def handle_filter():
    sentences = _parse_html_sentences(request.args['block'])
    filters = [get_filter_value(sent) for sent in sentences]
    do_censor = reduce(lambda x, y: x and y, filters)

    for sentence, do_filter in zip(sentences, filters):
        print(f'{sentence}:\n {sentence}')

    response = Response()
    response.headers['Do-Censor'] = [str(do_censor)]
    content = {"Do-Censor": [str(do_censor)]}

    return jsonify(content)


def _parse_html_sentences(content):
    errors = []
    sentences = []

    try:
        markup = "html.parser"
        soup = BeautifulSoup(content, markup)
        text_content = ' '.join(soup.text.split())
        sentences = [sent for sent in map(str.strip, text_content.split('.')) if sent]

    except:
        errors.append("No content!")
        print(*errors)

    return sentences


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

