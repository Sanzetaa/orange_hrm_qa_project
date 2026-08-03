from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddEmploymentStatusPage(BasePage):
    HEADER = (By.XPATH, "//h6[text()='Add Employment Status']")
    NAME_INPUT = (By.XPATH, "//label[text()='Name']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
    SUCCESS_TOAST = (By.XPATH, "//div[contains(@class,'oxd-toast--success')]//p[contains(@class,'oxd-text--toast-message')]")


    def page_is_displayed(self):
        return self.find_visible(self.HEADER)

    def type_name(self, name):
        self.type(self.NAME_INPUT, name)

    def click_save(self):
        self.click(self.SAVE_BUTTON)

    def get_success_message(self):
        return self.find_visible(self.SUCCESS_TOAST, timeout=10).text

    