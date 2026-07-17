from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class JobTitlesPage(BasePage):
    HEADER = (By.XPATH, "//h6[text()='Job Titles']")
    RESULT_TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']/div[contains(@class,'oxd-table-card')]")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    ADD_JOB_HEADER = (By.XPATH, "//h6[text()='Add Job Title']")

    def page_is_displayed(self):
        return self.find_visible(self.HEADER)

    def get_result_rows(self):
        try:
            return self.find_all_visible(self.RESULT_TABLE_ROWS, timeout=5)
        except Exception:
            return []
        
    def click_add_button(self):
        self.click(self.ADD_BUTTON)

    def add_job_header_is_visible(self):
        return self.find_visible(self.ADD_JOB_HEADER)

    