"""Handles Orange HRM Website"""

import pyperclip
import pyautogui
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebElement:

    def __init__(self, log: object) -> None:
        
        self.driver = Chrome()
        self.log = log


    def open_website(self):
        """Open Orange HRM Website"""
        try:
            self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
            self.log.register_info('Page opened successfully!')
        except Exception as error:
            self.log.register_error("Exception ocurred when opening page: %s" % error)
    

    def wait_element(self, element: str) -> bool:
        """Wait for element appear on page"""
        try:
            wait = WebDriverWait(self.driver, 10)
            item = wait.until(EC.visibility_of_element_located((By.XPATH, element))).get_attribute("value")
            if item != '':
                return True
        except Exception as error: 
            self.log.register_error("Element does not exists. Error -  %s" % error)
            return False


    def login(self, user: str, password:str):
        """Login on website"""

        try:
            sleep(2)
            login_filed = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
            login_filed.click()
            login_filed.send_keys(user)

            sleep(3)
            pwd_field = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
            pwd_field.click()
            pwd_field.send_keys(password)

            login_btn = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
            login_btn.click()

            ini_dashb_xpath =  '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span'
            ini_dashboard_exists = self.wait_element(ini_dashb_xpath)
            
            if ini_dashboard_exists:
                self.log.register_info('Login made successfully')
                return True
        
        except  Exception as error:
            self.log.register_error("Exception ocurred when loging into page: %s" % error)
            raise error


    def open_recruitment_page(self):
        """Select 'Recruitment' option on sidebar menu"""

        try:
            recruitment_option = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a')
            recruitment_option.click()
        
        except Exception as error:
            self.log.register_error("Exception ocurred when opening recruitment page: %s" % error)

    
    def fill_form(self, candidate_info: dict, resume_path: str) -> bool:
        """ Insert candidate information """

        try:
            add_btn = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
            add_btn.click()

            form_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div'
            if self.wait_element(form_xpath):

                # Insert name
                candidate_name = candidate_info["full_name"]
                candidate_name = candidate_name.split(" ")
                name_field = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]')
                fields = name_field.find_elements(By.TAG_NAME, 'input')
                i = 0
                for field in fields:
                    field.send_keys(candidate_name[i])
                    i+= 1

                # fill vacancy:
                try:
                    sleep(3)
                    vacancy_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div[2]/i'
                    self.wait_element(vacancy_xpath)
                    vacancy_field = self.driver.find_element(By.XPATH, vacancy_xpath)
                    vacancy_field.click()

                    sleep(2)
                    vacancy_options = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]')
                    options = vacancy_options.find_elements(By.TAG_NAME, 'div')
                    for option in options:
                        if option.text == candidate_info["vacancy"]:
                            option.click()
                            sleep(2)
                            pass
                except:
                    pass


                # fill email
                email_field = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input')
                email_field.send_keys(candidate_info["email"])

                # fill contact number
                contact_field = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input')
                contact_field.send_keys(candidate_info["contact_number"])

                # Insert candidate resume
                uploade_btn = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div/div/div/div[2]/div')
                uploade_btn.click()
                sleep(4)

                pyperclip.copy(resume_path)
                pyautogui.hotkey("ctrl", "v")
                sleep(2)
                pyautogui.press('tab')
                sleep(2)
                pyautogui.press('tab')
                sleep(1)
                pyautogui.press('enter')
                sleep(2)

                # fill keywords
                keywords = candidate_info["keywords"].replace(";", ",")
                keyword_field = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[5]/div/div[1]/div/div[2]/input')
                keyword_field.send_keys(keywords)

                save_btn = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]')
                save_btn.click()
            
            sleep(3)
            self.log.register_info('Candidate added!')
        except Exception as error:
            self.log.register_error("Exception ocurred while insertint informations: %s" % error)


    def new_candidate(self):
        """Click on button to open new form"""
        try:
            candidates_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]'
            if self.wait_element(candidates_xpath):
                candidates_btn = self.driver.find_element(By.XPATH, candidates_xpath)
                candidates_btn.click()
                sleep(3)
                self.log.register_info('Opening new form to register new candidate...')
        except Exception as error:
             self.log.register_error("Could not return to open new form -  %s" % error)

