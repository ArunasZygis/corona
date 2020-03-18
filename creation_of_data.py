import shelve


def update_data(new_data):  # method used to update table
    s = shelve.open("corona")
    s["corona"] = new_data
    s.close()


def display_data():
    s = shelve.open("corona")  # method used to display table
    corona_data = s["corona"]
    s.close()
    return corona_data


if __name__ == '__main__':
    print(display_data())
