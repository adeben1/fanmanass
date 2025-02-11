from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

from utils import logger, CustomException

def scrape_fantasy_analytics(url):
    """Scrapes player data using Selenium."""
    try:
        logger.info(f"Scraping data from {url} using Selenium")
        driver_path = r"C:\Users\adelosreyes.benitez\proyectos\libraries\chromedriver-win64\chromedriver.exe"
        driver = webdriver.Chrome(service=Service(driver_path))

        options = webdriver.ChromeOptions()

        driver.get(url)

        # Handle cookie pop-up (adapt the selector if necessary)
        try:
            accept_cookies_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,
                '#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay > div > button.css-y8g67k'))
            )
            accept_cookies_button.click()
            logger.info("Accepted cookies.")
        except Exception as e:
            logger.warning(f"Cookie popup not found or couldn't be clicked: {e}")

        # Wait for the table to load (adjust timeout as needed)
        try:  # Use a try-except block for more robust error handling
            table = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "table.custom-table")) #Or xpath, classname, etc. according to your needs
            )
        except Exception as e:  #If there is a timeout or the table cannot be located
            logger.exception("Error finding the table element: %s", e)
            driver.quit()  #Close the browser in case of error during page load
            raise CustomException("Timeout waiting for table or table not found. Check your selector and the page source.") from e

        # Extract headers
        headers = [th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")]

        # Extract data rows
        rows = []
        for row in table.find_elements(By.TAG_NAME, "tr")[1:]:  # Skip header row if any
            rows.append([cell.text.strip() for cell in row.find_elements(By.TAG_NAME, "td")])

        df = pd.DataFrame(rows, columns=headers)

        logger.info("Scraping completed successfully")
        driver.quit()  # Close the browser
        return df

    except Exception as e:
        logger.exception("An unexpected error occurred during scraping: %s", e)
        if "driver" in locals(): #Avoid failing if driver cannot be instantiated
            driver.quit() # Close the browser if there is an unexpected error and the driver has been created
        raise