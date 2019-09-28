from flask import Flask, request, jsonify
from filters_utils import get_filter_value
app = Flask("implement-ai")

@app.route('/')
def default():

    a = int(request.args.get('a', '4508071504'))
    b = int(request.args.get('b', '-1'))
    c = get_filter_value(a, b)
    print(a)
    print(a)
    print(b)
    return str(c)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)