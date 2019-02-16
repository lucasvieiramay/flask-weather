from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    template = 'index.html'
    if request.method == "POST":
        zipcode = request.form.get('zipcode')
    return render_template(template)


@app.route('/test')
def test():
    return 'test'
