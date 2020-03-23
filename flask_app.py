from flask import Flask, render_template, url_for, redirect, request

from database_creation_logic import display_data, update_data
from data_scraping_logic import get_corona_virus_data
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

heading = "Main page with button"


@app.route('/')
def index():
    return render_template('index.html', heading=heading)


# @app.route('/table_updated')  # used for update table
# def return_updated_table():
#     countries = get_corona_virus_data()  # not good option!
#     update_data(countries)
#     return render_template('table_updated.html', countries=countries)


@app.route('/table/<int:update>')
def display_table(update):
    if update == 1:
        print("updating with new data")
        update_data(get_corona_virus_data("corona_table_today"))
        new_url = url_for("display_table", update=0)
        return redirect(new_url)
    else:
        print("using old data")

    countries = display_data()
    return render_template('table.html', countries=countries)


@app.route('/search', methods=('GET', 'POST'))
def search():
    searched_keyword = request.form['title']
    converted_kwd_to_lowercase = searched_keyword.lower()
    list_for_search = display_data()
    results = []

    if converted_kwd_to_lowercase == '':
        return redirect('/')

    for sublist in list_for_search[1:]:
        if converted_kwd_to_lowercase in str(sublist).lower():
            results.append(sublist)
            print("Country is added!")

    if not results:
        return redirect('/table/0')

    print(results)
    return render_template("search.html", search_result=results)


@app.route('/yesterday_data')
def get_yesterday_data():
    countries = get_corona_virus_data('corona_table_yesterday')
    return render_template('yesterday_data.html', yesterday_results=countries)


if __name__ == '__main__':  # it can be run Only directly.
    app.run(debug=True)
