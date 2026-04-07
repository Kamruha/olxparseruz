# OLX Car Parser

A Python web scraping project that parses car listings from OLX Uzbekistan (olx.uz).

## Description

This script scrapes car listings from OLX Uzbekistan, filters them by price range, removes duplicates, and saves the results to a CSV file.

Features:
- Paginated scraping (default: 25 pages)
- Price range filtering (user input)
- Duplicate removal using unique URLs
- CSV export
- Error handling with try/except
- Random delays (1-3 seconds) to avoid blocking
- Configurable output directory

## Requirements

pip install requests beautifulsoup4


## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
Open main.py and set your output directory:
work_dir = r'C:\Your\Path\Here'
Run the script:
python main.py
Enter minimum and maximum price when prompted (without spaces, e.g., 10000000)
Results will be saved to olx.csv in your specified directory
Output
CSV file contains:

Title - car name
Price - price in UZS (cleaned)
Location - city/region
Link - full URL to the listing
Configuration
Edit these variables in main.py:

work_dir = r'C:\Your\Path\Here'  # Output directory
BASE_URL = 'https://www.olx.uz/transport/legkovye-avtomobili/'  # Target URL
MAX_PAGES = 26  # Number of pages to scrape
Notes
Random delay: 1-3 seconds between requests
User-Agent: Mozilla/5.0
Timeout: 10 seconds per request
Duplicate detection: uses cleaned URL (without query parameters)

Also update `requirements.txt`:
requests beautifulsoup4