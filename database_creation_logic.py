import shelve


def get_updated_table_data(new_data):
    """
    Method to create and update table with the last data in the database.

    :rtype: list
    :param new_data: Old list of data by countries in the database.
    :return: List of data by countries in the database.
    """
    s = shelve.open("corona")
    s["corona"] = new_data
    s.close()


def use_old_table_data():
    """
    Method to display the last updated table from the database.

    :rtype: list
    :return: List of data by countries in the database.
    """
    s = shelve.open("corona")
    corona_data = s["corona"]
    s.close()
    return corona_data


if __name__ == '__main__':
    print(use_old_table_data())
