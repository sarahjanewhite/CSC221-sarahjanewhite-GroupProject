# THIS FILE IS SIMPLY MY JUPYTER NOTEBOOK IN A CONDENSED FORMAT WITH MINIMAL COMMENTS #
# THIS IS A PERSONAL CONTRIBUTION AND IS NOT NECESSARY FOR THE FINAL PROJECT #
# LAST EDIT : SAT, JULY 13TH #

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

url = "https://en.m.wikipedia.org/wiki/List_of_best-selling_PlayStation_4_video_games"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
else:
    print("Failed to retrieve the webpage.")
    exit()

tables = soup.find_all('table', class_='wikitable plainrowheaders sortable static-row-numbers')

if tables:
    rows = tables[0].find_all('tr')

    games = []
    copies_sold = []
    release_dates = []
    genres = []
    developers = []
    publishers = []

    for row in rows[1:]:  # Skip header row
        cells = row.find_all(['td', 'th'])

        if len(cells) == 6:
            game = cells[0].get_text(strip=True)
            copy_sold_raw = cells[1].get_text(strip=True)
            release_date = cells[2].get_text(strip=True)
            genre = cells[3].get_text(strip=True)
            developer = cells[4].get_text(strip=True)
            publisher = cells[5].get_text(strip=True)

            # Clean up copies sold using regex
            copy_sold_clean = re.sub(r'\[.*?\]', '', copy_sold_raw)

            games.append(game)
            copies_sold.append(copy_sold_clean)
            release_dates.append(release_date)
            genres.append(genre)
            developers.append(developer)
            publishers.append(publisher)

    df = pd.DataFrame({
        'Game': games,
        'Copies Sold': copies_sold,
        'Release Date': release_dates,
        'Genre': genres,
        'Developer': developers,
        'Publisher': publishers
    })

    file_path = 'CSC221-webscrape-data.csv'
    df.to_csv(file_path, index=False)

    if os.path.exists(file_path):
        print(f"CSV file saved successfully: '{file_path}'")
    else:
        print(f"Error saving CSV file: Could not save '{file_path}'")
else:
    print("No tables found on the webpage.")
