from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from filters_utils import get_filter_value


app = Flask(__name__)

@app.route('/')
def default():

    #
    # a = int(request.args.get('a', '4508071504'))
    # b = int(request.args.get('b', '-1'))
    # c = get_filter_value(a, b)
    # print(a)
    # print(a)
    # print(b)
    # return str(c)
    return "You had me at hello"


@app.route('/filter')
def handle_filter():
    sentences = _parse_html_sentences(request.args['block'])
    for sentence in sentences:
        print(get_filter_value(sentence))

    return ""


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

