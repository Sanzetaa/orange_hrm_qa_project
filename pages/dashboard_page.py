from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    DASHBOARD_HEADER = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    ADMIN_MENU = (By.XPATH, "//span[normalize-space()='Admin']")

    def dashboard_is_visible(self):
        return self.find_visible(self. DASHBOARD_HEADER)
    
    def click_admin_menu(self):
        self.click(self.ADMIN_MENU)

    