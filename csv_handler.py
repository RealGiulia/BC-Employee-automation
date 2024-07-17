"""file implements CsvHandler class"""

import pandas as pd
import requests
import os

class CsvHandler:

    def __init__(self, folder: str, log: object):
        csv_folder = os.getcwd() + folder
        self.filename = os.path.join(csv_folder, "candidatos.csv")
        self.log = log
        if not os.path.exists(csv_folder):
            os.mkdir(csv_folder)

    
    def get_file(self):
        """ Download csv file and store on indicated folder"""

        try:
            file = requests.get("https://workshop.botcity.dev/assets/candidatos.csv")
            with open(self.filename, 'wb') as f:
                f.write(file.content)
            
            self.log.register_info("CSV file downloaded successfully!")

        except Exception as error:
            self.log.register_error("Error while doing CSV download. Error %s" % error)

        
    def read_csv(self) -> object:
        """Open csv file download and return a list of dict containg all the data of csv"""

        try:
            data = pd.read_csv(self.filename)
            data_dict = data.to_dict('records')
            self.log.register_info("CSV data inserted in a dict.")
             
            return data_dict
        except Exception as error:
            self.log.register_error("Error while doing CSV download. Error %s" % error)
            raise error

