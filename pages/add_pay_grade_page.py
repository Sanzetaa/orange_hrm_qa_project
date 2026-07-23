from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddPayGradePage(BasePage):
    HEADER = (By.XPATH, "//h6[text()='Add Pay Grade']")

    def page_is_displayed(self):
        return self.find_visible(self.HEADER)