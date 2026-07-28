from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddPayGradePage(BasePage):
    HEADER = (By.XPATH, "//h6[text()='Add Pay Grade']")
    NAME_INPUT = (By.XPATH, "//label[text()='Name']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")
    SUCCESS_TOAST = (By.XPATH, "//div[contains(@class,'oxd-toast--success')]//p[contains(@class,'oxd-text--toast-message')]")
    EDIT_PAY_GRADE_HEADER =(By.XPATH, "//h6[text()='Edit Pay Grade']")

    def page_is_displayed(self):
        return self.find_visible(self.HEADER)

    def edit_page_is_displayed(self):
        return self.find_visible(self.EDIT_PAY_GRADE_HEADER)

    def type_name(self, name):
        self.type(self.NAME_INPUT, name)

    def click_save(self):
        self.click(self.SAVE_BUTTON)

    def get_success_message(self):
        return self.find_visible(self.SUCCESS_TOAST, timeout=10).text
