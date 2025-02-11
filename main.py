import os

from dotenv import load_dotenv

from utils import CustomException, logger
from web_scraper import scrape_fantasy_analytics


if __name__ == "__main__":
    try:
        logger.info("Application started")
        url = "https://www.analiticafantasy.com/fantasy-la-liga/puja-ideal"

        load_dotenv() # carga variables de entorno
        DEVICE_IP = os.getenv("DEVICE_IP")

        # app_data = scrape_fantasy_app(DEVICE_IP, "app.package.name")  # Replace app package name
        web_data = scrape_fantasy_analytics(url)
        # report = process_data(app_data, web_data)
        # generate_report(report)  # Could save to a file or display directly
    except CustomException as e:  # Handle exceptions appropriately
        logger.exception("A critical error occurred: %s", e) # Log top-level exceptions
    finally:
        device.app_stop("app.package.name")  # If using uiautomator2. Change if necessary for Appium
