from data_scraping_logic import CoronaTable


def get_sorted_table_by_country(scraped_table_list: CoronaTable) -> CoronaTable:
    """
    Method to get and display countries in the table sorted by Countries column(ascending order).

    :param scraped_table_list: List of of the corona virus countries by selected day.
    :return: Returns a list sorted by Countries column.
    """
    table_sorted_by_countries_asc = scraped_table_list
    return sorted(table_sorted_by_countries_asc)
