from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class AdminPage(BasePage):
    ADMIN_HEADER = (By.XPATH, "//h6[text()='Admin']")
    USERNAME_INPUT = (By.XPATH,  "//label[text()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    USER_ROLE_DROPDOWN = (By.XPATH, "//label[text()='User Role']/""ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//label[text()='Employee Name']/ancestor::div[contains(@class,'oxd-input-group')]//input")

    STATUS_DROPDOWN = (By.XPATH, "//label[text()='Status']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]",)
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESET_BUTTON = (By.XPATH, "//button[@type='reset']")
    RESULT_TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']/div[contains(@class,'oxd-table-card')]",)
    NO_RECORDS_TEXT = (By.XPATH, "//span[text()='No Records Found']")

    FIRST_ROW_USERNAME_CELL = (By.XPATH, "(//div[@class='oxd-table-body']/div[contains(@class,'oxd-table-card')])[1]""//div[contains(@class,'oxd-table-cell')][2]")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    ORANGEHRM_LINK = (By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']")

    def admin_page_is_displayed(self):
        return self.find_visible(self.ADMIN_HEADER)
    
    def search_username(self, username, timeout=10):
        self.type(self.USERNAME_INPUT, username)
        self.click(self.SEARCH_BUTTON, timeout)

    def get_first_result_username(self):
        return self.get_text(self.FIRST_ROW_USERNAME_CELL)
    
    def search_username_out_of_list(self):
        return self.get_text(self.NO_RECORDS_TEXT)
    
    def no_record_text_is_displayed(self):
        return self.find_visible(self.NO_RECORDS_TEXT)
    
    def click_add_button(self):
        self.click(self.ADD_BUTTON)

    def click_orangeHRM_link(self):
        self.click(self.ORANGEHRM_LINK)
    
    

    

    
    