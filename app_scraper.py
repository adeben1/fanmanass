import uiautomator2 as u2
from utils import logger, CustomException

def connect_to_device(device_ip=None, device_serial=None):
    """Connects to the Android device.

    Args:
        device_ip: The IP address of the device (for Wi-Fi connection).
        device_serial:  The serial number of the device (for USB connection).

    Returns:
        A uiautomator2 device object.

    Raises:
        CustomException: If the connection fails.
    """
    try:
        if device_ip:
            device = u2.connect(device_ip)
        elif device_serial:
            device = u2.connect(device_serial)
        else:
            device = u2.connect()  # Tries to connect to a default device
        logger.info("Connected to device: %s", device.serial)
        return device
    except Exception as e:
        logger.error("Could not connect to device: %s", e)
        raise CustomException(f"Could not connect to device: {e}") from e # Chain exceptions

def scrape_fantasy_app(device, package_name):
    """Scrapes data from the Fantasy app and returns a Pandas DataFrame."""
    try:
        logger.info("Starting Fantasy app scraping")
        d = connect_to_device() # Call the function. You may want to store your IP or serial in the .env file and retrieve it from there
        d.app_start(package_name)
        # ... (Your app scraping logic using uiautomator2) ...
        # Example:
        # data = {'player': [], 'points': [], 'cost': []} #Data dictionary
        # elements = device(resourceId="some.id").get_text() # Example element selection, adapt as needed
        # Parse the relevant screen elements and populate the dictionary
        # ...

        # Example simulated user interaction to get more data
        # if d(text="Next Page").exists:  #Adapt as required
        #    d(text="Next Page").click()
        #    # ... extract data from the new page
        # ...
        d.app_stop(package_name) # Stop the app when finished
        logger.info("Completed Fantasy app scraping")  # Add logging
        # return pd.DataFrame(data) #Return dataframe with the parsed data
    except Exception as e:
        logger.exception("Error during app scraping: %s", e)
        raise  # Re-raise if needed
