import openpyxl
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from logger_setup import setup_logger
from utils import count_search_phrases, check_contains_money, download_picture


class AlJazeeraBot:
    def __init__(self):
        """Initialize the AlJazeeraBot with default settings and configurations."""
        self.base_url = "https://www.aljazeera.com/"
        self.category_url = "https://www.aljazeera.com/news/"
        self.xlsx_file = "news_data.xlsx"
        self.search_phrase = "Netanyahu"
        
        # Setup Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.log_file = "tbots_logs.log"
        self.logger = setup_logger(self.log_file)

    def run(self):
        """Run the bot: open website, search news, select category, and extract data."""
        try:
            self.logger.info("Starting Al Jazeera Bot...")
            self.open_website()
            self.search_news()
            self.select_news_category()
            self.extract_news_data()
        except Exception as e:
            self.logger.exception("An error occurred during the bot execution: {}".format(str(e)))
        finally:
            self.driver.quit()

    def open_website(self):
        """Open the Al Jazeera website."""
        self.logger.info("Opening Al Jazeera website...")
        self.driver.get(self.base_url)

    def search_news(self):
        """Search for news articles using the specified search phrase."""
        try:
            search_input = self.wait_for_element("//input[@type='search']")
            search_input.send_keys(self.search_phrase)
            search_input.submit()
            self.logger.info("Search successful.")
        except Exception as e:
            self.logger.error(f"Error during search: {str(e)}")

    def select_news_category(self):
        """Navigate to the news category page."""
        try:
            self.logger.info("Navigating to the news category page...")
            self.driver.get(self.category_url)
            self.logger.info("News category page loaded successfully.")
        except Exception as e:
            self.logger.error(f"Error navigating to the news category page: {str(e)}")

    def extract_news_data(self):
        """Extract data from news articles and save it to an Excel file."""
        self.logger.info("Extracting news data...")
        try:
            articles = self.wait_for_elements("//article")
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.append(["Title", "Date", "Description", "Picture Filename", "Search Phrase Count", "Contains Money"])

            for article in articles:
                title = self.get_element_text(article, ".//h1 | .//h2 | .//h3")
                date = self.get_element_text(article, ".//time")
                description = self.get_element_text(article, ".//p")
                picture_url = self.get_element_attribute(article, ".//img", "src")
                picture_filename = download_picture(picture_url)
                search_phrase_count = count_search_phrases(self.search_phrase, title, description)
                contains_money = check_contains_money(title, description)
                ws.append([title, date, description, picture_filename, search_phrase_count, contains_money])
            
            wb.save(self.xlsx_file)
            self.logger.info("News data saved to 'news_data.xlsx'.")
        except Exception as e:
            self.logger.error(f"Error extracting news data: {str(e)}")

    def get_element_text(self, parent_element, xpath):
        """Get text from an element located by XPath."""
        try:
            element = parent_element.find_element(By.XPATH, xpath)
            return element.text if element else ""
        except Exception as e:
            self.logger.error(f"Error getting text from element with XPath '{xpath}': {str(e)}")
            return ""

    def get_element_attribute(self, parent_element, xpath, attribute):
        """Get attribute value from an element located by XPath."""
        try:
            element = parent_element.find_element(By.XPATH, xpath)
            return element.get_attribute(attribute) if element else ""
        except Exception as e:
            self.logger.error(f"Error getting attribute '{attribute}' from element with XPath '{xpath}': {str(e)}")
            return ""

    def wait_for_element(self, xpath):
        """Wait for a single element to be visible on the page."""
        self.logger.info(f"Waiting for element with XPath {xpath}...")
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def wait_for_elements(self, xpath):
        """Wait for multiple elements to be visible on the page."""
        self.logger.info(f"Waiting for elements with XPath {xpath}...")
        return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))

