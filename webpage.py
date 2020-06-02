import flask
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def get_home():
    return flask.render_template('index2.html')

@app.route('/cal', methods=['GET', 'POST'])
def index():
    return flask.render_template('index.html')


@app.route('/get_no')
def get_values():
    value1 = flask.request.args.get('val1')
    value2 = flask.request.args.get('val2')
    return flask.jsonify({'data': f'<p>The result is: {value1 + value2}</p>'})


if __name__ == '__main__':
    app.run(debug=True)
