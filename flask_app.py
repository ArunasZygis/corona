from flask import Flask, render_template
from main import get_coronavirus_data
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

heading = "Main page with button"

@app.route('/')
def index():
    return render_template('index.html', heading=heading)

@app.route('/table')
def return_table():
    countries = get_coronavirus_data()
    return render_template('table.html', countries=countries)

if __name__ == '__main__': #it can be run Only directly.
    app.run(debug = True)