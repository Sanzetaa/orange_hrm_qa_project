from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PayGradesPage(BasePage):
    HEADER = (By.XPATH, "//h6[text()='Pay Grades']")
    RESULT_TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']/div[contains(@class,'oxd-table-card')]")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")

    def page_is_displayed(self):
        return self.find_visible(self.HEADER)
    
    def get_result_rows(self):
        try:
            return self.find_all_visible(self.RESULT_TABLE_ROWS, timeout=5)
        except Exception:
            return []

    def click_add_button(self):
        self.click(self.ADD_BUTTON)