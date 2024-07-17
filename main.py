
from csv_handler import CsvHandler
from logger import Logger
from user_input import INPUT_READER
from web import WebElement
from resume import Resume



#setup of environment
config = INPUT_READER()
log_path = config.parser("LOG_FOLDER")
csv_path = config.parser("CSV_FOLDER")

log = Logger(log_path)
csv_handler = CsvHandler(csv_path,log)
portal = WebElement(log)
resume_gen = Resume(log)

csv_handler.get_file()
data = csv_handler.read_csv()

portal.open_website()
login_done = portal.login('Admin', 'admin123')
if login_done:
    portal.open_recruitment_page()
    for i in data:
        resume_path = resume_gen.generate_resume(i)
        portal.fill_form(i,resume_path)
        portal.new_candidate()
    
    log.register_info("Candidates added successfully!")
    portal.driver.close()

