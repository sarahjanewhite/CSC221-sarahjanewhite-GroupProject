import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.m.wikipedia.org/wiki/List_of_best-selling_PlayStation_4_video_games'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='wikitable')

filename = 'CSC221-webscrape-data.csv'
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    rows = table.find('tbody').find_all('tr')
    for row in rows:
        cols = row.find_all(['td', 'th'])
        cols = [col.text.strip() for col in cols]
        csvwriter.writerow(cols)

print(f'CSV file "{filename}" has been created.')
