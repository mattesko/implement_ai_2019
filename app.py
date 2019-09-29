from flask import Flask, request, Response, jsonify
from bs4 import BeautifulSoup
# from filters_utils import get_filter_value
from functools import reduce
from flask_cors import CORS
from google_vision import google_visions
import ast


app = Flask(__name__)
CORS(app)

@app.route('/')
def default():
    return "You had me at hello"


@app.route('/filter', methods = ['POST'])
def handle_filter():
    sentences = (request.get_json())
    do_censor = [get_filter_value(sent) for sent in sentences]
    # do_censor = [True for _ in sentences]

    for sentence, do_filter in zip(sentences, do_censor):
        print(f'{sentence}:\n {str(do_filter)}')

    return jsonify(do_censor)


@app.route('/img')
def handle_images():
    """
    Function that parses the url input and does Google API inference on them.
    NOTE: THE URLS PASSED IN MUST NOT HAVE '&' CHARACTER. THOSE SHOULD BE REPLACED BY '%26' 
    :return: list of booleans for whether to obfuscate (True) or not (False).
    """
    # Get the list of urls that is passed in through the endpoint
    sentences = _parse_html_urls(request.args['block'])
    # Convert the string into a list of urls
    sentences = ast.literal_eval(sentences.split()[0])
    # Send list of urls
    temp = google_visions(sentences)
    # return the boolean values
    return str(temp)

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


def _parse_html_urls(sentences):
    for i in sentences:
        print(i)
    return sentences

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
