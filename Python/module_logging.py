import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = '%m/%d/%Y %H:%M:%S')
"""
By default, logger is called the root logger
Good practice is to use create own logger in a module

example in helper.py
-----
import logging

logger = logging.getLogger('__name__')
logger.info('hello from helper')
-----
"""

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#create handler
stream_h = logging.StreamHandler()
file_h = loggiing.FileHandler('file.log')

#level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter