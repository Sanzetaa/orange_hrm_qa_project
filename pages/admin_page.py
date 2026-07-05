from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminPage(BasePage):
    ADMIN_HEADER = (By.XPATH, "//h6[text()='Admin']")

    def admin_page_is_displayed(self):
        return self.find_visible(self.ADMIN_HEADER)
    
    