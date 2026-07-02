from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/"

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    def load(self):
        self.open(self.URL)
        self._wait_for_page_ready()

    def _wait_for_page_ready(self, timeout=10):
        self.find_visible(self.USERNAME_INPUT, timeout)
        self.find_visible(self.PASSWORD_INPUT, timeout)
        self.find_visible(self.LOGIN_BUTTON, timeout)

    def wait_for_dashboard(self, timeout=10):
        self.wait_for_url_contains("dashboard", timeout)

    def valid_credential_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def wrong_credential_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def invalid_username_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def invalid_password_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def blank_username_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def blank_password_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def both_blank_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def both_fields_uppercase_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def maximum_characters_length_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    