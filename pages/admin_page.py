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
    RESET_BUTTON = (By.XPATH, "//button[normalize-space()='Reset']")
    RESULT_TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']/div[contains(@class,'oxd-table-card')]",)
    NO_RECORDS_TEXT = (By.XPATH, "//span[text()='No Records Found']")

    FIRST_ROW_USERNAME_CELL = (By.XPATH, "(//div[@class='oxd-table-body']/div[contains(@class,'oxd-table-card')])[1]""//div[contains(@class,'oxd-table-cell')][2]")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    ORANGEHRM_LINK = (By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']")
    ADD_HEADER = (By.XPATH, "//h6[text()='Add User']")

    FIRST_ROW_CHECKBOX = (By.XPATH, "(//div[@class='oxd-table-body']/div[contains(@class,'oxd-table-card')])[1]//input[@type='checkbox']")
    DELETE_SELECTED_BUTTON = (By.XPATH, "//button[normalize-space()='Delete Selected']")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
    TRASH_BUTTON = (By.XPATH, "//i[@class='oxd-icon bi-trash']")
    SUCCESS_DELETE_MESSAGE = (By.XPATH, "//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']")

    USER_MANAGEMENT_DROPDOWN = (By.XPATH, "//span[normalize-space()='User Management']")
    USERS_MENU_ITEM = (By.XPATH, "//a[normalize-space()='Users']")

    JOB_DROPDOWN = (By.XPATH, "//span[normalize-space()='Job']")
    JOB_TITLES_MENU_ITEM = (By.XPATH, "//a[normalize-space()='Job Titles']")
    PAY_GRADES_MENU_ITEM = (By.XPATH, "//a[normalize-space()='Pay Grades']")

    def click_pay_grades_menu_item(self):
        self.click(self.PAY_GRADES_MENU_ITEM)

    def admin_page_is_displayed(self):
        return self.find_visible(self.ADMIN_HEADER)
    
    def search_username(self, username, timeout=10):
        self.type(self.USERNAME_INPUT, username)
        self.click(self.SEARCH_BUTTON, timeout)

    def get_first_result_username(self):
        return self.get_text(self.FIRST_ROW_USERNAME_CELL)
    
    def search_username_out_of_list(self):
        return self.get_text(self.NO_RECORDS_TEXT)
    
    def select_user_role(self, role_text):
        self.click(self.USER_ROLE_DROPDOWN)
        option = (By.XPATH, f"//div[@role='listbox']//span[text()='{role_text}']")
        self.click(option)

    def fill_employee_name(self, name):
        self.type(self.EMPLOYEE_NAME_INPUT, name)
        suggestion = (By.XPATH, "//div[@role='option'][1]")
        self.click(suggestion)

    def select_status(self, status_text):
        self.click(self.STATUS_DROPDOWN)
        option = (By.XPATH, f"//div[@role='listbox']//span[text()='{status_text}']")
        self.click(option)

    def click_reset(self):
        self.click(self.RESET_BUTTON)

    def get_username_field_value(self):
        return self.get_value(self.USERNAME_INPUT)
    
    def no_record_text_is_displayed(self):
        return self.find_visible(self.NO_RECORDS_TEXT)
    
    def click_add_button(self):
        self.click(self.ADD_BUTTON)

    def add_user_page_is_displayed(self):
        return self.find_visible(self.ADD_HEADER)
    
    def get_result_rows(self):
        try:
            return self.find_all_visible(self.RESULT_TABLE_ROWS, timeout=5)
        except Exception:
            return []
    

    def select_first_row_checkbox(self):
        self.js_click(self.FIRST_ROW_CHECKBOX)
    

    def click_delete_selected(self):
        self.click(self.DELETE_SELECTED_BUTTON)

    def confirm_delete(self):
        self.click(self.CONFIRM_DELETE_BUTTON)

    def click_user_management_dropdown(self):
        self.click(self.USER_MANAGEMENT_DROPDOWN)

    def click_users_menu_item(self):
        self.click(self.USERS_MENU_ITEM)

    def click_job_dropdown(self):
        self.click(self.JOB_DROPDOWN)

    def click_job_titles_menu_item(self):
        self.click(self.JOB_TITLES_MENU_ITEM)

    def click_orangeHRM_link(self):
        self.click(self.ORANGEHRM_LINK)
    
    

    

    
    