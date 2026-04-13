from bs4 import BeautifulSoup
import requests
import csv
from time import sleep
from random import randint
import os

# Set working directory
work_dir = r'C:\Your\Path\Here'  # Change this to your actual path
os.chdir(work_dir)
print(f"Working directory: {os.getcwd()}")

# Parser settings
BASE_URL = 'https://www.olx.uz/transport/legkovye-avtomobili/'
MAX_PAGES = 26

# User input
min_price = int(input("Enter min price: "))
max_price = int(input("Enter max price: "))
print("Filtering by price...")

# Set to store unique links (to avoid duplicates)
seen_links = set()

# Open file for writing
output_file = os.path.join(work_dir, 'olx.csv')

with open(output_file, 'w', newline="", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Location", "Link"])

    # Iterate through pages
    for page in range(1, MAX_PAGES):
        url = f'{BASE_URL}?page={page}'
        headers = {'User-Agent': 'Mozilla/5.0'}

        # Send request; skip page on network error
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.encoding = 'utf-8'
        except requests.exceptions.RequestException as e:
            print(f"Error on page {page}: {e}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', attrs={'data-cy': 'l-card'})

        # If no cards, pages are finished
        if not cards:
            print(f"Pages ended at page {page}")
            break

        # Process each card
        for card in cards:
            title = card.find('h4', class_='css-hzlye5')
            price = card.find('p', class_='css-blr5zl')
            location = card.find('p', class_='css-1b24pxk')
            link_tag = card.find('a', class_='css-1tqlkj0')

            # Get title text
            title = title.text.strip() if title else 'N/A'

            # Get price text and clean it
            price = price.text.strip() if price else 'N/A'
            price = price.replace('сум', '').replace('Договорная', '').replace('Обмен', '').strip()
            price_num_str = price.replace(' ', '')

            # Skip if price is not a number
            if not price_num_str.isdigit():
                continue
            price_num = int(price_num_str)

            # Price filter
            if price_num < min_price or price_num > max_price:
                continue

            # Process link
            link = 'https://www.olx.uz' + link_tag.get('href') if link_tag else 'N/A'
            link = link.split("?")[0]  # Remove query params from URL

            # Get location
            location = location.text.strip() if location else 'N/A'

            # Skip duplicates
            if link in seen_links:
                continue
            seen_links.add(link)

            # Write to CSV
            writer.writerow([title, price, location, link])
            print(f"Page: {page} | {title} | {price}")

        # Progress output every 5 pages
        if page % 5 == 0:
            print(f"Progress: page {page}/{MAX_PAGES}")

        # Pause to avoid blocking (random 1-3 seconds)
        sleep(randint(1, 3))

print(f"\nDone! Found {len(seen_links)} listings")
print(f"File saved: {output_file}")
