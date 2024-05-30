## AlJazeera News Scraper Bot
This Python script creates an AlJazeera bot that scrapes news data from the AlJazeera website and saves the extracted information into an Excel workbook. The bot performs a search for a specified phrase, navigates to the relevant news category, and extracts data such as titles, dates, descriptions, and image URLs from the news articles.

## Features
- Opens the AlJazeera website.
- Searches for news articles based on a specified search phrase.
- Navigates to the news category page.
- Extracts data from news articles.
- Saves the extracted data into an Excel file.

## Requirements
- Python 3.8+
- openpyxl
- selenium
- ChromeDriver (compatible with your installed version of Chrome)

## Setup
1. Clone the repository
    $ git clone https://github.com/yourusername/aljazeera-news-scraper.git
    $ cd aljazeera-news-scraper
2. Install the required Python packages:
    $ pip install -r requirements.txt
3. Download ChromeDriver and place it in a directory included in your system's PATH.

## Configuration
Before running the script, ensure you have configured the following files:
1. logger_setup.py - A module to set up logging.
2. utils.py - A module containing utility functions:
    -count_search_phrases: Counts occurrences of the search phrase.
    -check_contains_money: Checks if the content contains money-related terms.
    -download_picture: Downloads and saves images from URLs.

## Usage
Run the script using the following command:
  - python main.py

## Code Overview
# AlJazeeraBot Class
  # __init__(self):
  Initializes the bot with default settings and configurations:

  - self.base_url: Base URL for AlJazeera.
  - self.category_url: URL for the news category page.
  - self.xlsx_file: Filename for the Excel file.
  - self.search_phrase: Search phrase to look for in the news articles.
  - self.driver: Selenium WebDriver instance.
  - self.wait: WebDriverWait instance.
  - self.log_file: Log file name.
  - self.logger: Logger instance.

  # run(self)
  Main method to run the bot:

  - Opens the AlJazeera website.
  - Performs a search using the specified search phrase.
  - Navigates to the news category page.
  - Extracts data from news articles and saves it to an Excel file.

  # open_website(self)
  - Opens the AlJazeera website.

  # search_news(self)
  - Searches for news articles using the specified search phrase.

  # select_news_category(self)
  - Navigates to the news category page.

  # extract_news_data(self)
  - Extracts data from news articles and saves it to an Excel file.

  # get_element_text(self, parent_element, xpath)
  - Gets text from an element located by XPath.

  # get_element_attribute(self, parent_element, xpath, attribute)
  - Gets attribute value from an element located by XPath.

  # wait_for_element(self, xpath)
  - Waits for a single element to be visible on the page.

  # wait_for_elements(self, xpath)
  - Waits for multiple elements to be visible on the page.

## Logging
The bot uses logging to record its activities. Logs are saved to 'tbots_logs.log' by default.

## Error Handling
The bot includes error handling to catch and log exceptions that occur during execution.

## Contributing
Contributions are welcome. Please submit a pull request or open an issue to discuss your changes.
