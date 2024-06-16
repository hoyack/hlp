# utils/logger.py

import logging
import os
import time

# Create the /log directory if it doesn't exist
log_directory = 'log'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Get the current Unix timestamp
timestamp = int(time.time())

# Define the log file path with the timestamp
log_file_path = os.path.join(log_directory, f'{timestamp}.log')

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('main_logger')
