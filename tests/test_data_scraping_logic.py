
import data_scraping_logic


def test_get_website_response_status_code_positive_case():
    expected_status_code = 'STATUS IS OK: 200'
    actual_status_code = data_scraping_logic.get_website_response_status_code()

    assert expected_status_code == actual_status_code, 'Wrong Status Code!'

