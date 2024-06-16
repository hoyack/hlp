import logging
import sys
import os
import time

def setup_logger(name, log_dir, level=logging.INFO):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    timestamp = int(time.time())
    log_file = os.path.join(log_dir, f"{timestamp}.log")

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    # Add console handler to log to console as well
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger('main_logger', 'log')
