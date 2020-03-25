import shelve

from data_scraping_logic import CoronaTable


def save_new_table_data(new_data: CoronaTable):
    """
    Method to save newly acquired data in the database.

    :param new_data: Old list of data by countries in the database.
    :return: List of data by countries in the database.
    """
    s = shelve.open("corona")
    s["corona"] = new_data
    s.close()


def get_corona_data_from_database() -> CoronaTable:
    """
    Method to display the last updated table from the database.

    :return: List of data by countries in the database.
    """
    s = shelve.open("corona")
    corona_data = s["corona"]
    s.close()
    return corona_data


if __name__ == '__main__':
    print(get_corona_data_from_database())
