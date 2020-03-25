from flask import Flask, render_template, url_for, redirect, request

from date_selection import DataSource
from database_creation_logic import get_corona_data_from_database, save_new_table_data
from data_scraping_logic import get_website_response_status_code, get_data_from_website
from flask_bootstrap import Bootstrap

from table_sorting_logic import get_sorted_table_by_country

app = Flask(__name__)

Bootstrap(app)

heading = "Main page with button"
get_website_response_status_code()


@app.route('/')
def index_page():
    """
    Returns page index.html from the templates folder with main page information.

    :return: index.html page.
    """
    return render_template('index.html', heading=heading)


# @app.route('/table_updated')  # used for update table
# def return_updated_table():
#     countries = get_corona_virus_data()  # not good option!
#     update_data(countries)
#     return render_template('table_updated.html', countries=countries)


@app.route('/table/<int:update>')
def main_table_page(update):
    """
    Method to return table.html page from the templates folder with a Corona virus cases table.

    :type update: int
    :param update: the variable of the page shows which page to return and what methods to call:
    1- table_updated.html,
    0 - table.html page.

    :return: table.html page.
    """
    if update == 1:
        print("updating with new data")
        corona_countries_list = get_data_from_website(DataSource.TODAY_TABLE)
        save_new_table_data(corona_countries_list)
        new_url = url_for("main_table_page", update=0)
        return redirect(new_url)
    else:
        print("using old data")

    countries = get_corona_data_from_database()
    return render_template('table.html', countries=countries)


@app.route('/search', methods=('GET', 'POST'))
def search_results_page():
    """
     Method to return a search.html page from the templates folder with search results.

    :return: search.html page.
    """
    searched_keyword = request.form['title']
    converted_kwd_to_lowercase = searched_keyword.lower()
    countries_list_for_search = get_corona_data_from_database()
    search_results = []

    if converted_kwd_to_lowercase == '':
        return redirect('/')

    for sublist in countries_list_for_search[1:]:
        if converted_kwd_to_lowercase in str(sublist).lower():
            search_results.append(sublist)
            print("Country is added!")

    if not search_results:
        return redirect('/table/0')

    return render_template("search.html", search_result=search_results)


@app.route('/yesterday_data')
def get_yesterday_data():
    """
    Method to return yesterday_data.html page from the templates folder with yesterday's corona virus results.

    :return: yesterday_data.html page.
    """
    corona_table_countries = get_data_from_website(DataSource.YESTERDAY_TABLE)
    # corona_tables = scrape_website_data('main_table_countries_yesterday',"https://www.worldometers.info/coronavirus/")
    # corona_table_countries = create_list_of_countries(corona_tables)
    return render_template('yesterday_data.html', yesterday_results=corona_table_countries)


@app.route('/sorted_table')
def get_sorted_table():
    """
    Method to return sorted_table.html page from the templates folder with corona virus results sorted by Countries
    column (ascending order).

    :return: sorted_table.html page.
    """
    countries_list = get_data_from_website(DataSource.YESTERDAY_TABLE)
    sorted_countries_list = get_sorted_table_by_country(countries_list)
    return render_template('sorted_table.html', sorted_results_list=sorted_countries_list)


if __name__ == '__main__':  # it can be run Only directly.
    app.run(debug=True)
