```
# OLX Car Parser

A Python web scraper that collects car listings from OLX Uzbekistan and exports them to CSV.

---

## Overview

This script scrapes car listings from [olx.uz](https://www.olx.uz), filters them by price range,
removes duplicates, and saves the results to a CSV file for further analysis.

---

## Features

| Feature | Description |
|--------|-------------|
| Multi-page scraping | Scrapes up to 25 pages of listings |
| Price filtering | Filters results by user-defined min/max price |
| Duplicate removal | Detects duplicates using unique listing URLs |
| Error handling | Skips failed pages without crashing the script |
| Random delays | Waits 1–3 seconds between requests to avoid blocking |
| CSV export | Saves results to a structured `.csv` file |

---

## Technologies Used

- **Python** — core language
- **requests** — HTTP requests
- **BeautifulSoup** — HTML parsing

---

## Installation

    pip install requests beautifulsoup4

---

## Setup

1. Install dependencies:

       pip install -r requirements.txt

2. Open `main.py` and set your output directory:

       work_dir = r'C:\Your\Path\Here'

3. Run the script:

       python main.py

4. Enter minimum and maximum price when prompted (without spaces, e.g. `10000000`)

Results will be saved to `olx.csv` in your specified directory.

---

## Output

The CSV file contains the following columns:

| Column | Description |
|--------|-------------|
| Title | Car name and model |
| Price | Price in UZS (cleaned) |
| Location | City or region |
| Link | Full URL to the listing |

---

## Configuration

Edit these variables in `main.py` to customize the scraper:

    work_dir = r'C:\Your\Path\Here'  # Output directory
    BASE_URL = 'https://www.olx.uz/transport/legkovye-avtomobili/'  # Target URL
    MAX_PAGES = 26  # Number of pages to scrape

---

## Notes

- Random delay of 1–3 seconds between requests to avoid getting blocked
- Requests use a 10-second timeout to prevent hanging on slow responses
- Duplicate detection is based on cleaned URLs (without query parameters)
- User-Agent header is set to mimic a real browser

---

## License

MIT
```
