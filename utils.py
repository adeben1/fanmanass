
import logging
import os



# Configure logging
log_file = os.path.join(os.path.dirname(__file__), "fanmanass.log") # Log to file relative to the script's location

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,  # Or DEBUG for more verbose logging
    format="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

class CustomException(Exception):
    pass
