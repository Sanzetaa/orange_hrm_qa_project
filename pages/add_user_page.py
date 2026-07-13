from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddUserPage(BasePage):
    HEADER = (By.XPATH, "//h6[text()='Add User']")

    USER_ROLE_DROPDOWN = (By.XPATH, "//label[text()='User Role']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//label[text()='Employee Name']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    STATUS_DROPDOWN = (By.XPATH, "//label[text()='Status']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]")
    USERNAME_INPUT = (By.XPATH, "//label[text()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Password']/ancestor::div[contains(@class,'oxd-input-group')]//input[@type='password']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//label[text()='Confirm Password']/ancestor::div[contains(@class,'oxd-input-group')]//input[@type='password']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[normalize-space()='Cancel']")

    def add_user_page_is_displayed(self):
        return self.find_visible(self. HEADER)
    
    def select_user_role(self, role_text):
        self.click(self.USER_ROLE_DROPDOWN)
        option = (By.XPATH, f"//div[@role='listbox']//span[text()='{role_text}']")
        self.click(option)

    def select_status(self, status_text):
        self.click(self.STATUS_DROPDOWN)
        option = (By.XPATH, f"//div[@role='listbox']//span[text()='{status_text}']")
        self.click(option)

    def type_employee_name(self, name):
        self.type(self.EMPLOYEE_NAME_INPUT, name)
        suggestion = (By.XPATH, "//div[@role='option'][1]")
        self.click(suggestion)

    def type_username(self, username):
        self.type(self.USERNAME_INPUT, username)

    def type_password(self, password):
        self.type(self.PASSWORD_INPUT, password)
        self.type(self.CONFIRM_PASSWORD_INPUT, password)

    def click_save(self):
        self.click(self.SAVE_BUTTON)
    
    