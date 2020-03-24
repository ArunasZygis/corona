import shelve


def get_updated_table_data(new_data):  # method used to update table
    s = shelve.open("corona")
    s["corona"] = new_data
    s.close()


def use_old_table_data():  # method used to display old table data
    s = shelve.open("corona")
    corona_data = s["corona"]
    s.close()
    return corona_data


if __name__ == '__main__':
    print(use_old_table_data())
