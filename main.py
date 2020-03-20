import requests
from bs4 import BeautifulSoup


def get_corona_virus_data(select_day):
    url = 'https://www.worldometers.info/coronavirus/'
    corona_website_url = requests.get(url)
    answer_code = corona_website_url.status_code
    current_url_status = str(answer_code)

    if answer_code == requests.codes.ok:
        print('Status is OK: ' + current_url_status)
    else:
        print('Status is not OK: ' + current_url_status)

    parse_website_data = corona_website_url.text
    soup = BeautifulSoup(parse_website_data, 'html.parser')  # html.parser - Standard Python parsing library
    print("\n")
    corona_table_today = soup.find('table', {'id': 'main_table_countries_today'})
    corona_table_yesterday = soup.find('table', {'id': 'main_table_countries_yesterday'})

    if select_day == "corona_table_today":
        corona_table = corona_table_today
    else:
        corona_table = corona_table_yesterday


    table_rows = corona_table.find_all('tr')
    countries = []
    for idx, row in enumerate(table_rows):
        if idx == 0:
            trows_data = row.find_all('th')
            print(trows_data)
        else:
            trows_data = row.find_all('td')

        row_data = []
        for td in trows_data:
            row_data.append(td.text)
        countries.append(row_data)
    return countries

# if __name__ == '__main__':
#     print(get_corona_virus_data())

# def show_table():
#     pprint(list(zip(*countries)))
#
#
#
# show_table()


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
