import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.m.wikipedia.org/wiki/List_of_best-selling_PlayStation_4_video_games'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='wikitable')
data = []

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all(['td', 'th'])
    cols = [col.text.strip() for col in cols]
    data.append(cols)

print("Printing First 10 Items...")
for row in data[1:12]:  # This is needed to ignore the headers
    print(row)

filename = 'CSC221-webscrape-data.csv'
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in data:
        csvwriter.writerow(row)

print(f'\nCSV file "{filename}" has been created.')
