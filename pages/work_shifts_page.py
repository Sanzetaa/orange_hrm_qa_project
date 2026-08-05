from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WorkShiftsPage(BasePage):
    WORK_SHIFT_HEADER = (By.XPATH, "//h6[text()='Work Shifts']")
    RESULT_TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']/div[contains(@class,'oxd-table-card')]")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")

    #Add Work Shift
    ADD_WORK_SHIFT_HEADER = (By.XPATH, "//h6[text()='Add Work Shift']")
    NAME_INPUT = (By.XPATH, "//label[text()='Shift Name']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    SUCCESS_TOAST = (By.XPATH, "//div[contains(@class,'oxd-toast--success')]//p[contains(@class,'oxd-text--toast-message')]")
    CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")

    def page_is_displayed(self):
        return self.find_visible(self.WORK_SHIFT_HEADER)

    def get_result_rows(self):
        try:
            return self.find_all_visible(self.RESULT_TABLE_ROWS, timeout=5)
        except Exception:
            return []

    def click_add_button(self):
        self.click(self.ADD_BUTTON)

    def add_page_is_displayed(self):
        return self.find_visible(self.ADD_WORK_SHIFT_HEADER)

    def type_name(self, name):
        self.type(self.NAME_INPUT, name)

    def click_save(self):
        self.click(self.SAVE_BUTTON)

    def get_success_message(self):
        return self.find_visible(self.SUCCESS_TOAST, timeout=10).text

    

