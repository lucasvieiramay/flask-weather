import pyowm
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)


owm = pyowm.OWM('a583ecc7ffde60bc4a4ce437b0a6b3a4')


@app.route('/', methods=['GET', 'POST'])
def home():
    template = 'index.html'
    if request.method == "POST":
        zipcode = request.form.get('zipcode')
        observation = owm.weather_at_zip_code(zipcode=zipcode, country='US')
        response = observation.get_weather()
        temperature = response.get_temperature('celsius')
        return render_template('result.html', temp=temperature['temp'])
    return render_template(template)


@app.route('/test')
def test():
    return 'test'
