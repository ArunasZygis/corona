from typing import List

import requests
from bs4 import BeautifulSoup, element

from date_selection import DataSource

CoronaTable = List[List[str]]


def get_website_response_status_code() -> str:
    """
    Method to get website response status code.

    :return: Website response status code.
    """
    web_url = 'https://www.worldometers.info/coronavirus/'
    corona_website_url = requests.get(web_url)
    website_response = corona_website_url.status_code
    current_url_status = str(website_response)

    if website_response == requests.codes.ok:
        current_response_status = 'STATUS IS OK: ' + current_url_status
        print(current_response_status)
        return current_response_status
    else:
        current_response_status = 'Website is DOWN:' + current_url_status
        print(current_response_status)
        return current_response_status


def scrape_website_data(date_selection: DataSource, url: str) -> element.Tag:
    """
    Method to scrape website and get data of corona virus infected countries by selected day.

    :param date_selection: Date input to choose the right data source(for Today table or Yesterday table).
    :param url: Website url to scrape data from.
    :return: Beautiful Soup object to create a table of corona virus results.
    """
    website_url = requests.get(url)
    soup = BeautifulSoup(website_url.text, 'html.parser')  # html.parser - Standard Python parsing library

    if date_selection == DataSource.TODAY_TABLE:
        select_corona_table = soup.find('table', {'id': 'main_table_countries_today'})
    elif date_selection == DataSource.YESTERDAY_TABLE:
        select_corona_table = soup.find('table', {'id': 'main_table_countries_yesterday'})
    else:
        raise Exception("Wrong value for data_selection argument. Expected one of TODAY_TABLE/YESTERDAY_TABLE")
    return select_corona_table


def create_list_of_countries(select_corona_table: element.Tag) -> CoronaTable:
    """
    Method to get data from provided Beautiful Soup object and create a list of corona virus countries.


    :param select_corona_table: Beautiful Soup object.
    :return: List of the corona virus countries.
    """
    all_table_rows = select_corona_table.find_all('tr')
    countries = []
    for idx, row in enumerate(all_table_rows):
        if idx == 0:
            table_rows_data = row.find_all('th')
        else:
            table_rows_data = row.find_all('td')

        table_rows_data_list = []
        for countries_data in table_rows_data:
            table_rows_data_list.append(countries_data.text)
        countries.append(table_rows_data_list)
    return countries


# def get_table_rows_data(table_rows_data):
#     table_rows_data_list = []
#     for countries_data in table_rows_data:
#         table_rows_data_list.append(countries_data.text)
#     return table_rows_data_list

def get_data_from_website(date_selection: DataSource) -> CoronaTable:
    """
    Method to get and display countries in the table by selected data source.

    :param date_selection: Date input to choose the right data source.
    :return: Table of the corona virus countries by selected day.
    """
    web_url = 'https://www.worldometers.info/coronavirus/'
    table_element = scrape_website_data(date_selection, url=web_url)
    data_by_country = create_list_of_countries(table_element)
    return data_by_country

# total_cases_column = []
# new_cases_column = []
# total_deaths_column = []
# new_deaths_column = []
# total_recovered_column = []
# active_cases_column = []
# serious_column = []
# tot_cases_column = []
#
# for idx, cc in enumerate(table_rows):
#         if idx ==0:
#             countries_column.append(cc.text)
#         if idx == 1:
#             tot_cases_column.append(cc.text)
#         if idx == 2:
#             new_cases_column.append(cc.text)
#         if idx == 3:
#             total_deaths_column.append(cc.text)
#         if idx == 4:
#             new_deaths_column.append(cc.text)
#         if idx == 5:
#             total_recovered_column.append(cc.text)
#         if idx == 6:
#             active_cases_column.append(cc.text)
#         if idx == 7:
#             serious_column.append(cc.text)
#         else: tot_cases_column.append(cc.text)
#
#
#
#
# print(tot_cases_column)
