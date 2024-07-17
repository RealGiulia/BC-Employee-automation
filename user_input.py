"""Reads config.ini file"""

import configparser
import os


class INPUT_READER:

    def __init__(self):
        self.filepath = os.getcwd() + "/data/config.ini"
        self.config = configparser.ConfigParser()
        

    def parser(self, Item: str):
        self.config.read(self.filepath)
        value = self.config.get("INPUT", Item)
        return value

