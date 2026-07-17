from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddJobTitlePage(BasePage):
    HEADER = (By.XPATH, "//h6[text()='Add Job Title']")
    JOB_TITLE_INPUT = (By.XPATH, "//label[text()='Job Title']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    JOB_DESCRIPTION_TEXTAREA = (By.XPATH, "//label[text()='Job Description']/ancestor::div[contains(@class,'oxd-input-group')]//textarea")
    
    JOB_SPECIFICATION_ADD_LINK = (By.XPATH, "//label[text()='Job Specification']/ancestor::div[contains(@class,'oxd-input-group')]//input[@type='file']")

    NOTE_TEXTAREA = (By.XPATH, "//label[text()='Note']/ancestor::div[contains(@class,'oxd-input-group')]//textarea")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class,'oxd-toast--success')]//p[contains(@class,'oxd-text--toast-message')]")

    def page_is_displayed(self):
        return self.find_visible(self.HEADER)
    
    def type_job_title(self, title):
        self.type(self.JOB_TITLE_INPUT, title)

    def type_job_description(self, description):
        self.type(self.JOB_DESCRIPTION_TEXTAREA,description)

    def attach_job_specification(self, file_path):
        self.find(self.JOB_SPECIFICATION_ADD_LINK).send_keys(file_path)

    def type_note(self, note_text):
        self.type(self.NOTE_TEXTAREA, note_text)

    def click_save(self):
        self.click(self.SAVE_BUTTON)

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)

    def get_success_message(self):
        return self.find_visible(self.SUCCESS_MESSAGE, timeout=10).text


    