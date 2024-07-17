"""Implements Log class and its functionalities"""

import logging
import os
from datetime import date

class Logger:

    def __init__(self, log_folder: str) -> None:
        self.name = date.today().strftime("%m-%d-%y") + '-NewsSearcherLog.log'
        folder = os.getcwd() + log_folder
        self.filename = os.path.join(folder, self.name)
        if not os.path.exists(folder):
            os.makedirs(folder)
        logging.basicConfig(filename=self.filename,level=logging.NOTSET, format='%(asctime)s - %(levelname)s - %(message)s')


    def register_info(self, message):
        logging.info(message)


    def register_warn(self, message):
        logging.warning(message)

    
    def register_error(self, message):
        logging.exception(message)

