from bs4 import element
from mock import MagicMock, patch

from data_scraping_logic import get_website_response_status_code, scrape_website_data, create_list_of_countries
from date_selection import DataSource


def test_get_website_response_status_code_positive_case():
    expected_status_code = 'STATUS IS OK: 200'
    actual_status_code = get_website_response_status_code()

    assert expected_status_code == actual_status_code, 'Wrong Status Code!'


# negative case can be tested like assert False expected == actual? or if only has if statement? Why we don't check other values?
@patch('data_scraping_logic.requests.get')
def test_get_website_response_status_code_negative_case(mock_requests_get_method):
    magic_response = MagicMock()
    magic_response.status_code = 333
    mock_requests_get_method.return_value = magic_response

    expected_status_code = "Website is DOWN:333"
    actual_status_code = get_website_response_status_code()

    assert expected_status_code == actual_status_code


def test_scrape_website_data_positive_case():
    website_url = 'https://www.worldometers.info/coronavirus/'
    date_selection = DataSource.TODAY_TABLE
    expected_returned_element = element.Tag
    actual_returned_element = type(scrape_website_data(date_selection, website_url))

    assert expected_returned_element == actual_returned_element


def test_scrape_website_data_negative_case():
    website_url = 'https://www.worldometers.info/coronavirus/'
    date_selection = DataSource.YESTERDAY_TABLE
    expected_returned_element = element.Tag
    actual_returned_element = type(scrape_website_data(date_selection, website_url))

    assert expected_returned_element == actual_returned_element


def test_create_list_of_countries_positive_case():
    website_url = 'https://www.worldometers.info/coronavirus/'
    date_selection = DataSource.TODAY_TABLE
    table_element_to_create_table = scrape_website_data(date_selection, website_url)
    expected_returned_list = list
    actual_returned_list = type(create_list_of_countries(table_element_to_create_table))

    assert expected_returned_list == actual_returned_list


def test_create_list_of_countries_negative_case():
    website_url = 'https://www.worldometers.info/coronavirus/'
    date_selection = DataSource.YESTERDAY_TABLE
    table_element_to_create_table = scrape_website_data(date_selection, website_url)
    expected_returned_list = list
    actual_returned_list = type(create_list_of_countries(table_element_to_create_table))

    assert expected_returned_list == actual_returned_list
