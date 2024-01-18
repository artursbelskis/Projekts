import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

def scrape_page(soup, table):
    tables_elements = soup.find('tbody').find_all('tr', class_='standing-table__row')
    for tables_element in tables_elements:
        Place = tables_element.find('td', class_='standing-table__cell').text.strip()
        Teams = tables_element.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
        Points = tables_element.find('td', class_='standing-table__cell', attrs={'data-sort-value': True}).text.strip()
        Points = float(Points)
        table.append(
            {
                'Place': Place,
                'Teams': Teams,
                'Points': Points,
            }
        )

def find_team_info(table, team_name):
    for tables in table:
        if tables['Teams'].lower() == team_name.lower():
            return tables
    return None

url = 'https://www.skysports.com/la-liga-table'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

table = []

scrape_page(soup, table)

csv_file = open('La Liga Table.csv', 'w', encoding='utf-8', newline='')

writer = csv.writer(csv_file)

writer.writerow(['Place', 'Teams', 'Points'])

for tables in table:
    writer.writerow(tables.values())

csv_file.close()

df = pd.DataFrame(table)
df.to_excel('La Liga Table.xlsx', index=False)

team_name_input = input("Enter team name: ")
team_info = find_team_info(table, team_name_input)
if team_info:
    print(f"\nPlace: {team_info['Place']}\nTeam: {team_info['Teams']}\nPoints: {team_info['Points']}\n")
else:
    print("No such team was found. Please try again.")