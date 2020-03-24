import requests
from bs4 import BeautifulSoup, element


def get_website_response_status_code():
    """
    Method to get website response status code.

    :rtype: str
    :return: Website response status code.
    """
    web_url = 'https://www.worldometers.info/coronavirus/'
    corona_website_url = requests.get(web_url)
    answer_code = corona_website_url.status_code
    current_url_status = str(answer_code)

    if answer_code == requests.codes.ok:
        return print('Status is OK: ' + current_url_status)
    else:
        return print('Status is not OK: ' + current_url_status)


def scrape_website_data(date_selection, url):
    """
    Method to scrape website and get data of corona virus infected countries by selected day.

    :type date_selection: str
    :type url: str
    :param date_selection: Date input to choose the right table.
    :param url: Website url to scrape data from.
    :return: Beautiful Soup object.
    :rtype: bs4.element.Tag
    """
    website_url = requests.get(url)
    soup = BeautifulSoup(website_url.text, 'html.parser')  # html.parser - Standard Python parsing library

    if date_selection == "corona_table_today":
        select_corona_table = soup.find('table', {'id': 'main_table_countries_today'})
    else:
        select_corona_table = soup.find('table', {'id': 'main_table_countries_yesterday'})
    return select_corona_table


def create_list_of_countries(select_corona_table):
    """
    Method to get data from provided Beautiful Soup object and create a list of corona virus countries.

    :type select_corona_table: bs4.element.Tag
    :rtype: list
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

        row_data_list = []
        for td in table_rows_data:
            row_data_list.append(td.text)

        countries.append(row_data_list)
    return countries


def get_data_from_website(date_selection):
    """
    Method to get and display countries in the table by selected day.

    :rtype: list
    :return: List of the corona virus countries by selected day.
    :type date_selection: str
    """
    web_url = 'https://www.worldometers.info/coronavirus/'
    table_element = scrape_website_data(date_selection, url=web_url)
    data_by_country = create_list_of_countries(table_element)
    return data_by_country

# countries_column = []
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
