from flask import Flask, render_template

# from creation_of_data import display_data, update_data
from creation_of_data import display_data, update_data
from main import get_corona_virus_data
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

heading = "Main page with button"


@app.route('/')
def index():
    return render_template('index.html', heading=heading)


@app.route('/table_updated')  # used for update table
def return_updated_table():
    countries = get_corona_virus_data()  # not good option!
    update_data(countries)
    return render_template('table_updated.html', countries=countries)


@app.route('/table')
def display_table():
    countries = display_data()
    return render_template('table.html', countries=countries)


if __name__ == '__main__':  # it can be run Only directly.
    app.run(debug=True)
